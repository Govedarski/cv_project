from managers.auth_manager import AuthManager
from managers.helpers.manager_mixins import PromoteManagerMixin, LoginManagerMixin, GetManagerMixin
from models.user.employer_model import EmployerModel


class EmployerManager(PromoteManagerMixin, LoginManagerMixin, GetManagerMixin):
    MODEL = EmployerModel

    @classmethod
    def promote(cls, data, user_id):
        return super().promote(data, user_id)

    @classmethod
    def login(cls, data):
        user = super().login(data)
        if user.employer is None:
            return AuthManager.encode_token(user), user
        return AuthManager.encode_token(user.job_seeker), user.employer
