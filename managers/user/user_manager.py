from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from managers.auth_manager import AuthManager
from managers.helpers.manager_mixins import CreateManagerMixin, LoginManagerMixin, EditManagerMixin, GetManagerMixin
from managers.user.profile_manager import ProfileManager
from models.user.user_model import UserModel


class UserManager(CreateManagerMixin, LoginManagerMixin, EditManagerMixin, GetManagerMixin):
    model = UserModel

    @classmethod
    def register(cls, data):
        profile_data = data.get('profile_data', {})
        credentials_data = data.get('credentials')

        user = cls.create(credentials_data)
        ProfileManager.create(profile_data, user)
        token = AuthManager.encode_token(user)

        return token, user

    @classmethod
    def login(cls, data):
        user = super().login(data)
        return AuthManager.encode_token(user), user

    @classmethod
    def change_password(cls, data, user_id):
        user = cls.get_model().query.filter_by(id=user_id).first()
        if user and check_password_hash(user.password, data["old_password"]):
            user.password = data["new_password"]
            return user
        raise BadRequest("Wrong old password")
