from managers.auth_manager import auth
from managers.user.user_manager import UserManager
from resources.helpers.permision_functions import is_user_with_valid_id
from resources.helpers.resource_mixins import EditResourceMixin, GetResourceMixin
from schemas.request.users.authentication_schemas_in import IdentifiersSchemaIn
from schemas.response.users.user_schema_out import ExtendUserSchemaOut


class UserResource(EditResourceMixin, GetResourceMixin):
    MANAGER = UserManager
    SCHEMA_IN = IdentifiersSchemaIn
    SCHEMA_OUT = ExtendUserSchemaOut

    @auth.login_required
    def get(self, user_id, **kwargs):
        return super().get(user_id)

    @auth.login_required
    def put(self, user_id, **kwargs):
        return super().put(user_id, **kwargs)

    def check_permissions(self, current_user, *args, **kwargs):
        is_user_with_valid_id(current_user, **kwargs)