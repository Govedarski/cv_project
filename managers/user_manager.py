from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from constants.strings import IDENTIFIER, PASSWORD, EMAIL, USERNAME
from managers.auth_manager import AuthManager
from managers.helpers.manager_mixins import CreateManagerMixin
from managers.profile_manager import ProfileManager
from models.user_models import UserModel
from managers.helpers.decorators import handle_unique_constrain_violation


class UserManager(CreateManagerMixin):
    MODEL = UserModel
    CREDENTIALS_ERROR_MESSAGE = "Wrong credentials!"
    DEACTIVATED_USER = "Wrong credentials!"

    @classmethod
    @handle_unique_constrain_violation
    def register(cls, data):
        credentials_data = {EMAIL: data.pop(EMAIL),
                            USERNAME: data.get(USERNAME) and data.pop(USERNAME),
                            PASSWORD: data.pop(PASSWORD)}
        try:
            user = cls.create(credentials_data)
            token = AuthManager.encode_token(user)
            ProfileManager.create(data, user)

            return token, user

        except Exception as ex:
            raise ex

    @classmethod
    def login_user(cls, data):
        user = cls._login(data)
        return AuthManager.encode_token(user), user

    @classmethod
    def _login(cls, data):
        user = cls.get_model().query.filter_by(email=data[IDENTIFIER]).first() \
               or cls.get_model().query.filter_by(username=data[IDENTIFIER]).first()

        if user and user.password[0] == "!":
            raise BadRequest(cls.DEACTIVATED_USER)

        if user and check_password_hash(user.password, data[PASSWORD]):
            return user

        raise BadRequest(cls.CREDENTIALS_ERROR_MESSAGE)
