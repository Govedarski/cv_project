from abc import ABC, abstractmethod

from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import check_password_hash

from constants.strings import IDENTIFIER, PASSWORD, PAGE_NOT_FOUND
from managers.auth_manager import AuthManager
from managers.helpers.base_manager import BaseManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.image_manager import ImageManager
from models.user.user_model import UserModel


class CreateManagerMixin(BaseManager):
    @classmethod
    @handle_unique_constrain_violation
    def create(cls, data, user=None):
        if hasattr(cls.get_model(), "owner_id") and user:
            data["owner_id"] = user.id

        if cls.need_image_handler():
            return ImageManager.create_with_images(cls.get_model(), data)

        return cls.create_obj(cls.get_model(), data)


class PromoteManagerMixin(CreateManagerMixin):
    @classmethod
    def promote(cls, data, user_id):
        data["id"] = user_id
        user_subclass_instance = cls.create(data)
        token = AuthManager.encode_token(user_subclass_instance)

        return token, user_subclass_instance


class LoginManagerMixin(ABC):
    CREDENTIALS_ERROR_MESSAGE = "Wrong credentials!"
    DEACTIVATED_USER = "Wrong credentials!"

    @classmethod
    @abstractmethod
    def login(cls, data) -> UserModel:
        user = UserModel.query.filter_by(email=data[IDENTIFIER]).first() \
               or UserModel.query.filter_by(username=data[IDENTIFIER]).first()

        if user and user.password[0] == "!":
            raise BadRequest(cls.DEACTIVATED_USER)

        if user and check_password_hash(user.password, data[PASSWORD]):
            return user

        raise BadRequest(cls.CREDENTIALS_ERROR_MESSAGE)


class GetManagerMixin(BaseManager):
    def get(self, _id):
        instance = self._get_instance(_id)
        if not instance:
            raise NotFound

        return instance


class EditManagerMixin(BaseManager):
    @handle_unique_constrain_violation
    def edit(self, data, _id, **kwargs):
        instance = self._get_instance(_id)

        if self.need_image_handler():
            return ImageManager.edit_with_images(self.get_model(), data, instance)

        self.get_model().query.filter_by(id=instance.id).update(data)
        return instance
