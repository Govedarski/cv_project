from abc import ABC, abstractmethod

from sqlalchemy.exc import InvalidRequestError
from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import check_password_hash

from constants.strings import IDENTIFIER, PASSWORD, PAGE_NOT_FOUND
from managers.auth_manager import AuthManager
from managers.helpers.base_manager import BaseManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.file_manager import FileManager
from models.user.user_model import UserModel


class CreateManagerMixin(BaseManager):
    @classmethod
    @handle_unique_constrain_violation
    def create(cls, data, user=None):
        if hasattr(cls.get_model(), "owner_id") and user:
            data["owner_id"] = user.id

        file_manager = FileManager(cls.get_model())

        try:
            file_manager.create_file_links(data)
            instance = cls.create_obj(cls.get_model(), data)
        except Exception as ex:
            file_manager.delete_from_cloud(file_manager.names_of_created_files)
            raise ex
        finally:
            file_manager.delete_all_from_server()

        return instance


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

        file_manager = FileManager(self.get_model())
        file_manager.edit(instance)

        try:
            file_manager.create_file_links(data)
            self.get_model().query.filter_by(id=instance.id).update(data)
        except Exception as ex:
            file_manager.delete_from_cloud(file_manager.names_of_created_files)
            raise ex
        finally:
            file_manager.delete_all_from_server()

        file_manager.delete_old_file_from_cloud()

        return instance


class GetListManagerMixin(BaseManager):
    def get_list(self, filter_by, **kwargs):
        query = self.get_model().query
        for field, criteria in filter_by.items():
            if ".in" in field:
                field_name = field.split(".")[0]
                query = query.filter(getattr(self.get_model(), field_name).contains(criteria))
            else:
                current_criteria = {field: criteria}
                query = query.filter_by(**current_criteria)

        try:
            return query.all()
        except InvalidRequestError:
            # Invalid query string
            return []
