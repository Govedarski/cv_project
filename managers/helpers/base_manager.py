from werkzeug.exceptions import BadRequest

from db import db

# from services.s3_aws_service import s3
from utils import helpers
from managers.helpers.decorators import handle_unique_constrain_violation


# from utils.decorators import handle_unique_constrain_violation

class BaseManager:
    MODEL = None
    UNIQUE_CONSTRAINT_MESSAGE = "Unique constraint: Object already exist!"
    PERMISSION_DENIED_MESSAGE = "Permission denied!"
    _INSTANCE = None

    @classmethod
    def get_model(cls):
        return cls.MODEL

    def _get_instance(self, pk):
        if not self._INSTANCE:
            self._INSTANCE = helpers.get_or_404(self.get_model(), pk)
        return self._INSTANCE

    @staticmethod
    def create_obj(model, data, add_to_db=True):
        instance = model(**data)
        if add_to_db:
            db.session.add(instance)
            db.session.flush()
        return instance

    @classmethod
    def need_image_handler(cls):
        return hasattr(cls.get_model(), "get_all_image_field_names")





# class BaseManager:
#     MODEL = None
#     UNIQUE_CONSTRAINT_MESSAGE = "Unique constraint: Object already exist!"
#     PERMISSION_DENIED_MESSAGE = "Permission denied!"
#     _INSTANCE = None
#
#     # Todo to add attr for custom message for handle_unique
#     @handle_unique_constrain_violation
#     def create(self, data, user, **kwargs):
#         if not hasattr(self.get_model(), "creator_id") and user:
#             data["creator_id"] = user.id
#
#         if not hasattr(self.get_model(), "get_all_image_field_names"):
#             return self._create_obj(self.get_model(), data)
#
#         # return self._processed_with_photos(self.get_model(), data, add_to_db=add_to_db)
#
#     def get(self, pk, **kwargs):
#         return self._get_instance(pk)

    # def get_list(self, filter_by, **kwargs):
    #     query = self.get_model().query
    #     for field, criteria in filter_by.items():
    #         if ".in" in field:
    #             field_name = field.split(".")[0]
    #             query = query.filter(getattr(self.get_model(), field_name).contains(criteria))
    #         else:
    #             current_criteria = {field: criteria}
    #             query = query.filter_by(**current_criteria)
    #
    #     try:
    #         return query.all()
    #     except InvalidRequestError:
    #         # Invalid query string
    #         return []

    # @handle_unique_constrain_violation
    # def edit(self, data, pk, **kwargs):
    #     instance = self._get_instance(pk)
    #     if not hasattr(self.get_model(), "get_all_image_field_names"):
    #         self.get_model().query.filter_by(id=instance.id).update(data)
    #         return instance

        # return self._processed_with_photos(self.get_model(), data, instance)

    # def delete(self, pk, **kwargs):
    #     instance = self._get_instance(pk)
    #     if not hasattr(self.get_model(), "get_all_image_field_names"):
    #         self.get_model().query.filter_by(id=instance.id).delete()
    #         return None

        # return self._delete_with_photos(self.get_model(), instance)

    # def delete_image(self, pk, image_field_name, **kwargs):
    #     self._check_access(pk, **kwargs)
    #     instance = self._get_instance(pk)
    #     image_field_name_with_suffix = image_field_name + IMAGE_SUFFIX_IN_DB
    #     photo_url = getattr(instance, image_field_name_with_suffix)
    #     photo = get_photo_name_by_url(photo_url)
    #     if not photo:
    #         raise NotFound('Picture not found!')
    #
    #     self.get_model().query.filter_by(id=instance.id).update({image_field_name_with_suffix: None})
    #     s3.delete_photo(photo)
    #     return instance

    # def _get_instance(self, pk):
    #     if not self._INSTANCE:
    #         self._INSTANCE = helpers.get_or_404(self.get_model(), pk)
    #     return self._INSTANCE
    #
    # @staticmethod
    # def _create_obj(model, data):
    #     instance = model(**data)
    #     db.session.add(instance)
    #     db.session.flush()
    #     return instance

    # TODO: INTEGRATE S3 BUCKET FOR STORING PICTURES
    # def _processed_with_photos(self, model, data, instance=None, add_to_db=True):
    #     is_edit = bool(instance)
    #     image_field_names = model.get_all_image_field_names()
    #     photo_names = []
    #     paths = []
    #     previous_pictures = []
    #     try:
    #         for image_field_name in image_field_names:
    #             photo_str = data.pop(image_field_name + IMAGE_SUFFIX_IN_SCHEMA) \
    #                 if data.get(image_field_name + IMAGE_SUFFIX_IN_SCHEMA) else None
    #             extension = data.pop(image_field_name + EXTENSION_SUFFIX_IN_SCHEMA) \
    #                 if data.get(image_field_name + EXTENSION_SUFFIX_IN_SCHEMA) else None
    #             if not has_photo(photo_str, extension):
    #                 continue
    #
    #             if is_edit:
    #                 photo_url = getattr(instance, image_field_name + IMAGE_SUFFIX_IN_DB)
    #                 previous_picture = get_photo_name_by_url(photo_url)
    #                 previous_pictures.append(previous_picture)
    #
    #             photo_name, photo = create_photo(photo_str, extension)
    #             photo_names.append(photo_name)
    #             path = os.path.join(TEMP_DIR, photo_name)
    #             paths.append(path)
    #             save_file(path, photo)
    #
    #             photo_url = s3.upload_photo(path, photo_name)
    #             data[image_field_name + IMAGE_SUFFIX_IN_DB] = photo_url
    #
    #         if is_edit:
    #             model.query.filter_by(id=instance.id).update(data)
    #             [s3.delete_photo(previous_picture) for previous_picture in previous_pictures if previous_picture]
    #         else:
    #             instance = self._create_obj(model, data, add_to_db=add_to_db)
    #
    #     except Exception as ex:
    #         [s3.delete_photo(photo_name) for photo_name in photo_names]
    #         raise ex
    #     finally:
    #         [os.remove(path) for path in paths]
    #
    #     return instance
    #

    # TODO
    # @staticmethod
    # def _delete_with_photos(model, instance, **kwargs):
    #     image_field_names = model.get_all_image_field_names()
    #     photo_to_delete = []
    #
    #     for image_field_name in image_field_names:
    #         photo_name = get_photo_name_by_url(getattr(instance, image_field_name + IMAGE_SUFFIX_IN_DB))
    #         photo_to_delete.append(photo_name)
    #
    #     model.query.filter_by(id=instance.id).delete()
    #     [s3.delete_photo(photo) for photo in photo_to_delete if photo]







