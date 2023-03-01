from werkzeug.exceptions import Forbidden

from constants.strings import FORBIDDEN
from managers.auth_manager import auth
from managers.user.employer_manager import EmployerManager
from managers.user.job_seeker_manager import JobSeekerManager
from managers.user.user_manager import UserManager
from resources.helpers.permision_functions import is_user_with_valid_id
from resources.helpers.resource_mixins import BaseResource, LoginResourceMixin, EditResourceMixin
from schemas.request.users.authentication_schemas_in import LoginSchemaIn, RegisterSchemaIn, IdentifiersSchemaIn, \
    ChangePasswordSchemaIn
from schemas.response.users.employer_schema_out import EmployerSchemaOut
from schemas.response.users.job_seeker_schema_out import JobSeekerSchemaOut
from schemas.response.users.user_schema_out import ExtendUserSchemaOut, UserSchemaOut


class RegisterResource(BaseResource):
    MANAGER = UserManager
    SCHEMA_IN = RegisterSchemaIn
    SCHEMA_OUT = ExtendUserSchemaOut

    def post(self):
        data = self.get_data()
        token, user = self.get_manager().register(data)
        return self.create_login_response(token, user), 201


class ChangePasswordResource(BaseResource):
    MANAGER = UserManager
    SCHEMA_IN = ChangePasswordSchemaIn
    SCHEMA_OUT = UserSchemaOut

    @auth.login_required
    def put(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id, **kwargs)
        data = self.get_data()
        instance = self.get_manager()().change_password(
            data,
            user_id,
            **kwargs)

        return self.get_schema_out(instance=instance)().dump(instance), 200

    def check_permissions(self, current_user, *args, **kwargs):
        is_user_with_valid_id(current_user, **kwargs)


class LoginUserResource(LoginResourceMixin):
    MANAGER = UserManager
    SCHEMA_IN = LoginSchemaIn
    SCHEMA_OUT = ExtendUserSchemaOut

    def post(self):
        return super().post()


class LoginJobSeekerResource(LoginResourceMixin):
    MANAGER = JobSeekerManager
    SCHEMA_IN = LoginSchemaIn
    SCHEMA_OUT = JobSeekerSchemaOut

    def post(self):
        return super().post()


class LoginEmployerResource(LoginResourceMixin):
    MANAGER = EmployerManager
    SCHEMA_IN = LoginSchemaIn
    SCHEMA_OUT = EmployerSchemaOut

    def post(self):
        return super().post()
