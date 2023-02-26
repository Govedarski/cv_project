from managers.helpers.base_manager import BaseManager
from managers.helpers.manager_mixins import CreateManagerMixin
from models.profile_model import ProfileModel


class ProfileManager(CreateManagerMixin):
    MODEL = ProfileModel
    