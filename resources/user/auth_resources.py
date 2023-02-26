from sqlalchemy import null

from managers.user_manager import UserManager
from resources.helpers.resource_mixins import BaseResource, CreateResourceMixin
from schemas.request.users.authentication_schemas_in import RegisterSchemaIn, LoginSchemaIn
from schemas.response.users.user_schema_out import UserSchemaOut


class RegisterUserResource(CreateResourceMixin):
    MANAGER = UserManager
    SCHEMA_IN = RegisterSchemaIn
    SCHEMA_OUT = UserSchemaOut

    def post(self):
        data = self.get_data()
        token, user = self.get_manager().register(data)
        user = self.serialize_obj(user)
        return {"token": token, "user": user}, 201


class LoginUserResource(BaseResource):
    MANAGER = UserManager
    SCHEMA_IN = LoginSchemaIn
    SCHEMA_OUT = UserSchemaOut


    def post(self):
        data = self.get_data()
        token, user = self.get_manager().login_user(data)
        user = self.serialize_obj(user)
        return {"token": token, "user": user}, 200
