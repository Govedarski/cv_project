from abc import abstractmethod, ABC

from managers.auth_manager import auth
from resources.helpers.base_resource import BaseResource


class CreateResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: MANAGER, SCHEMA_IN and SCHEMA_OUT"""

    @abstractmethod
    def post(self, **kwargs):
        current_user = self.get_user()
        data = self.get_data()
        instances = self.get_manager()().create(
            data,
            current_user,
            **kwargs)
        return self.get_schema_out(instance=instances)(many=isinstance(instances, list)).dump(instances), 201


class GetResourceMixin(ABC, BaseResource):
    """Minimum required class attributes: SCHEMA_OUT"""

    @abstractmethod
    def get(self, pk, **kwargs):
        instance = self.get_manager()().get(pk, **kwargs)
        return self.get_schema_out(instance=instance)().dump(instance), 200
#
#
# class GetListResourceMixin(ABC, BaseResource):
#     """Minimum required class attributes: SCHEMA_OUT"""
#
#     @abstractmethod
#     def get(self, **kwargs):
#         obj_list = self.get_manager()().get_list(self.filter_by(), **kwargs)
#         return [self.get_schema_out(instance=instance)().dump(instance) for instance in obj_list if instance], 200
#
#     def filter_by(self):
#         return {}
#
#
# class EditResourceMixin(ABC, BaseResource):
#     """Minimum required class attributes: SCHEMA_OUT"""
#
#     @abstractmethod
#     def put(self, pk, **kwargs):
#         data = self.get_data()
#         instance = self.get_manager()().edit(data, pk, **kwargs)
#         return self.get_schema_out(instance=instance)().dump(instance), 200
#
#
# class DeleteResourceMixin(ABC, BaseResource):
#     @abstractmethod
#     def delete(self, pk, **kwargs):
#         self.get_manager()().delete(pk, **kwargs)
#         return None, 204
#
#
# class DeleteImageResourceMixin(ABC, BaseResource):
#     """Minimum required class attributes: IMAGE_FIELD_NAME, SCHEMA_OUT"""
#     IMAGE_FIELD_NAME = ""
#
#     @abstractmethod
#     def delete(self, pk, **kwargs):
#         instance = self.get_manager()().delete_image(pk, self.IMAGE_FIELD_NAME, **kwargs)
#         return self.get_schema_out(instace=instance)().dump(instance), 200
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
