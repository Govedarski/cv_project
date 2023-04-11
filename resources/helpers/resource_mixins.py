from abc import abstractmethod, ABC

from managers.auth_manager import auth
from resources.helpers.base_resource import BaseResource


class CreateResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: MANAGER, SCHEMA_IN and SCHEMA_OUT"""

    @abstractmethod
    def post(self, **kwargs):
        current_user = self.get_valid_current_user()
        data = self.get_data()
        instances = self.get_manager()().create(data, current_user)
        return self.serialize_obj(instances), 201


class LoginResourceMixin(ABC, BaseResource):
    @abstractmethod
    def post(self):
        data = self.get_data()
        token, user_data = self.get_manager().login(data)
        if not user_data:
            return self.create_login_response(token, user_data)
        return self.create_login_response(token, user_data), 200


class PromoteResourceMixin(ABC, BaseResource):
    @auth.login_required
    def post(self, user_id):
        self.get_valid_current_user(_id=user_id)
        data = self.get_data()
        token, user_subclass_instance = self.get_manager().promote(data, user_id)
        return self.create_login_response(token, user_subclass_instance)


class GetResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: MANAGER and SCHEMA_OUT"""

    @abstractmethod
    def get(self, _id, **kwargs):
        self.get_valid_current_user(_id=_id)
        instances = self.get_manager()().get(_id, **kwargs)
        return self.serialize_obj(instances, _id=_id, **kwargs), 200


class EditResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: MANAGER, SCHEMA_IN and SCHEMA_OUT"""

    @abstractmethod
    def put(self, _id, **kwargs):
        self.get_valid_current_user(_id=_id)
        data = self.get_data()
        instances = self.get_manager()().edit(
            data,
            _id,
            **kwargs)

        return self.serialize_obj(instances, _id=_id, **kwargs), 200

#
class GetListResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: SCHEMA_OUT"""

    @abstractmethod
    def get(self, **kwargs):
        obj_list = self.get_manager()().get_list(self.filter_by(), **kwargs)
        return [self.get_schema_out(instance=instance)().dump(instance) for instance in obj_list if instance], 200

    def filter_by(self):
        return {}



#
#
class DeleteResourceMixin(ABC, BaseResource):
    @abstractmethod
    def delete(self, _id, **kwargs):
        self.get_manager()().delete(_id, **kwargs)
        return {"deleted": True}, 200

#
# class DeleteImageResourceMixin(ABC, BaseResource):
#     """Minimum required class attributes: IMAGE_FIELD_NAME, SCHEMA_OUT"""
#     IMAGE_FIELD_NAME = ""
#
#     @abstractmethod
#     def delete(self, _id, **kwargs):
#         instance = self.get_manager()().delete_image(_id, self.IMAGE_FIELD_NAME, **kwargs)
#         return self.get_schema_out(instance=instance)().dump(instance), 200
#
#
# class RemoveIbanSpacesMixin:
#     def get_data(self):
#         data = super().get_data()
#         iban = data.get("iban")
#         if iban:
#             data["iban"] = data["iban"].replace(" ", "")
#
#         return data
