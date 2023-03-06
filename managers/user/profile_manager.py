from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, EditManagerMixin
from models.user.profile_model import ProfileModel


class ProfileManager(CreateManagerMixin, GetManagerMixin, EditManagerMixin):
    model = ProfileModel

    @classmethod
    def create(cls, data, user=None):
        data['id'] = user.id
        return super(ProfileManager, cls).create(data)
