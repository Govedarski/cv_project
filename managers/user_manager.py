from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from constants.strings import IDENTIFIER, PASSWORD
from db import db
from managers.auth_manager import AuthManager
from managers.base_manager import BaseManager
from models.user_models import UserModel
from utils.decorators import handle_unique_constrain_violation


class UserManager(BaseManager):
    MODEL = UserModel
    CREDENTIALS_ERROR_MESSAGE = "Wrong credentials!"
    DEACTIVATED_USER = "Wrong credentials!"

    @classmethod
    @handle_unique_constrain_violation
    def register(cls, data):
        user = cls.get_model()(**data)
        db.session.add(user)
        db.session.flush()
        return AuthManager.encode_token(user)

    @classmethod
    def login_user(cls, data):
        user = cls._login(data)
        return AuthManager.encode_token(user)

    @classmethod
    def _login(cls, data):
        user = UserModel.query.filter_by(email=data[IDENTIFIER]).first() \
               or UserModel.query.filter_by(username=data[IDENTIFIER]).first()

        if user and user.password[0] == "!":
            raise BadRequest(cls.DEACTIVATED_USER)

        if user and check_password_hash(user.password, data[PASSWORD]):
            return user

        raise BadRequest(cls.CREDENTIALS_ERROR_MESSAGE)