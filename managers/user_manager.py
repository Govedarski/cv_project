from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from constants.strings import IDENTIFIER, PASSWORD
from managers.auth_manager import AuthManager
from managers.helpers.manager_mixins import CreateManagerMixin
from models.user_models import UserModel
from managers.helpers.decorators import handle_unique_constrain_violation


class UserManager(CreateManagerMixin):
    MODEL = UserModel
    CREDENTIALS_ERROR_MESSAGE = "Wrong credentials!"
    DEACTIVATED_USER = "Wrong credentials!"

    @classmethod
    @handle_unique_constrain_violation
    def register(cls, data):
        user = super().create(data)
        return AuthManager.encode_token(user)

    @classmethod
    def login_user(cls, data):
        user = cls._login(data)
        return AuthManager.encode_token(user)

    @classmethod
    def _login(cls, data):
        user = cls.get_model().query.filter_by(email=data[IDENTIFIER]).first() \
               or cls.get_model().query.filter_by(username=data[IDENTIFIER]).first()

        if user and user.password[0] == "!":
            raise BadRequest(cls.DEACTIVATED_USER)

        if user and check_password_hash(user.password, data[PASSWORD]):
            return user

        raise BadRequest(cls.CREDENTIALS_ERROR_MESSAGE)
