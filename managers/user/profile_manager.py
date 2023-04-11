from managers.helpers.file_manager import FileManager
from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, EditManagerMixin
from models.user.profile_model import ProfileModel
from utils.helpers import get_file_name_by_url


class ProfileManager(CreateManagerMixin, GetManagerMixin, EditManagerMixin):
    MODEL = ProfileModel

    @classmethod
    def create(cls, data, user=None):
        data['id'] = user.id
        return super(ProfileManager, cls).create(data)

    def delete_profile_picture(self, _id):
        instance = self._get_instance(_id)
        old_file_name = get_file_name_by_url(instance.profile_picture_file_url)
        FileManager.delete_from_cloud([old_file_name])
        instance.profile_picture_file_url = None
        return instance
