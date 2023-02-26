from managers.user_manager import UserManager
from resources.helpers.resource_mixins import BaseResource
from schemas.request.users.authentication_schemas_in import RegisterSchemaIn, LoginSchemaIn


class RegisterUserResource(BaseResource):
    MANAGER = UserManager
    SCHEMA_IN = RegisterSchemaIn

    def post(self):
        data = self.get_data()
        token = self.get_manager().register(data)
        return {"token": token}, 201


class LoginUserResource(BaseResource):
    MANAGER = UserManager
    SCHEMA_IN = LoginSchemaIn

    def post(self):
        data = self.get_data()
        token = self.get_manager().login_user(data)
        return {"token": token}, 200
