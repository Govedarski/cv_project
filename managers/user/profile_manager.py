from managers.helpers.manager_mixins import CreateManagerMixin
from models.user.profile_model import ProfileModel


class ProfileManager(CreateManagerMixin):
    MODEL = ProfileModel

    @classmethod
    def create(cls, data, user=None):
        data['id'] = user.id
        return super(ProfileManager, cls).create(data)
