from flask import request

from constants import methods
from managers.auth_manager import auth
from managers.user.profile_manager import ProfileManager
from resources.helpers.permision_functions import is_user_with_valid_id
from resources.helpers.resource_mixins import GetResourceMixin, EditResourceMixin
from schemas.request.users.profile_schema_in import ProfileSchemaIn
from schemas.response.users.profile_schema_out import ProfileSchemaOut, PublicProfileSchemaOut


class ProfileResource(GetResourceMixin, EditResourceMixin):
    MANAGER = ProfileManager
    SCHEMA_IN = ProfileSchemaIn

    @auth.login_optional
    def get(self, user_id, **kwargs):
        return super().get(user_id, **kwargs)

    @auth.login_required
    def put(self, user_id):
        return super().put(user_id)

    # def delete(self):
    #     return super().delete()

    def get_schema_out(self, *args, **kwargs):
        user = self.get_valid_current_user(*args, **kwargs)
        _id = kwargs.get('_id', None)
        return ProfileSchemaOut if user and user.id == _id else PublicProfileSchemaOut

    def check_permissions(self, current_user, *args, **kwargs):
        if request.method == methods.PUT:
            is_user_with_valid_id(current_user, **kwargs)
