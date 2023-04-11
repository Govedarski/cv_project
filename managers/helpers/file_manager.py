import os
from copy import copy

from constants.file_suffix import FILE_SUFFIX_IN_SCHEMA, EXTENSION_SUFFIX_IN_SCHEMA, FILE_SUFFIX_IN_DB
from constants.roots import TEMP_DIR
from services.s3_aws_service import s3
from utils.helpers import has_file_data, get_file_name_by_url, create_file, save_file


class FileManager:
    def __init__(self, model):
        self.model = model
        self.old_instance = None
        self.names_of_created_files = []
        self.paths_of_created_files = []
        self.changed_file_field_names = []

    def edit(self, instance):
        self.old_instance = copy(instance)

    def create_file_links(self, data):
        for file_field_name in self.model.get_all_file_field_names():

            file_binary = (file_field_name + FILE_SUFFIX_IN_SCHEMA) in data.keys() \
                          and data.pop(file_field_name + FILE_SUFFIX_IN_SCHEMA)

            file_extension = (file_field_name + EXTENSION_SUFFIX_IN_SCHEMA) in data.keys() \
                and data.pop(file_field_name + EXTENSION_SUFFIX_IN_SCHEMA)

            if not has_file_data(file_binary, file_extension):
                continue

            file_name, file = create_file(file_binary, file_extension)
            self.names_of_created_files.append(file_name)
            path = os.path.join(TEMP_DIR, file_name)
            self.paths_of_created_files.append(path)
            save_file(path, file)

            self.changed_file_field_names.append(file_field_name)
            file_url = s3.upload_photo(path, file_name)
            data[file_field_name + FILE_SUFFIX_IN_DB] = file_url

    def delete_old_file_from_cloud(self):
        old_file_names = []

        for file_field_name in self.changed_file_field_names:
            file_url = getattr(self.old_instance, file_field_name + FILE_SUFFIX_IN_DB)
            if not file_url:
                continue
            old_file_name = get_file_name_by_url(file_url)
            old_file_names.append(old_file_name)

        self.delete_from_cloud(old_file_names)

    def delete_all_from_server(self):
        [os.remove(path) for path in self.paths_of_created_files]

    @staticmethod
    def delete_from_cloud(file_names):
        [s3.delete_photo(file_name) for file_name in file_names if file_name]

