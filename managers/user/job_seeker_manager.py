from managers.auth_manager import AuthManager
from managers.helpers.manager_mixins import PromoteManagerMixin, LoginManagerMixin, GetManagerMixin, EditManagerMixin
from models.user.job_seeker_model import JobSeekerModel


class JobSeekerManager(PromoteManagerMixin, LoginManagerMixin, GetManagerMixin, EditManagerMixin):
    model = JobSeekerModel

    @classmethod
    def promote(cls, data, user_id):
        return super().promote(data, user_id)

    @classmethod
    def login(cls, data):
        user = super().login(data)
        if user.job_seeker is None:
            return AuthManager.encode_token(user), user
        return AuthManager.encode_token(user.job_seeker), user.job_seeker
