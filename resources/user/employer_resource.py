from managers.auth_manager import auth
from managers.user.employer_manager import EmployerManager
from resources.helpers.permision_functions import is_user_with_valid_id
from resources.helpers.resource_mixins import PromoteResourceMixin, GetResourceMixin
from schemas.request.users.employer_schema_in import EmployerSchemaIn
from schemas.response.users.employer_schema_out import EmployerSchemaOut


class EmployerResource(PromoteResourceMixin, GetResourceMixin):
    MANAGER = EmployerManager
    SCHEMA_IN = EmployerSchemaIn
    SCHEMA_OUT = EmployerSchemaOut

    def post(self, user_id):
        return super().post(user_id)

    @auth.login_required
    def get(self, user_id, **kwargs):
        return super().get(user_id, **kwargs)

    def get_data(self):
        return {}

    def check_permissions(self, current_user, *args, **kwargs):
        is_user_with_valid_id(current_user, **kwargs)
