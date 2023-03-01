from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.user.profile_model import ProfileModel


class ProfileManager(CreateManagerMixin, GetManagerMixin):
    MODEL = ProfileModel

    @classmethod
    def create(cls, data, user=None):
        data['id'] = user.id
        return super(ProfileManager, cls).create(data)
