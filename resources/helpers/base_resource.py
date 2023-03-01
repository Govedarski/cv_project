from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest, Forbidden

from constants.strings import FORBIDDEN
from managers.auth_manager import auth
from managers.helpers.base_manager import BaseManager
from models.user.user_model import UserModel
from resources.helpers.decorators import admin_access_granted


class BaseResource(Resource):
    MANAGER = BaseManager
    ALL_ADMINS_ALLOWED = True
    SCHEMA_IN = None
    SCHEMA_OUT = None
    ALLOWED_ROLES = None

    def get_data(self, *args, **kwargs):
        """Validation is happened here so if you need to override this always call super
        or validate the schema on your own."""
        schema = self.get_schema_in(*args, **kwargs)
        data = request.get_json() if request.data else None
        many = getattr(schema, 'MANY', False) and isinstance(data, list)

        try:
            return schema(many=many).load(data) if data else {}
        except ValidationError as ex:
            raise BadRequest(ex.messages)

    def get_schema_in(self, *args, **kwargs):
        return self.SCHEMA_IN

    def get_schema_out(self, *args, **kwargs):
        return self.SCHEMA_OUT

    def get_manager(self, *args, **kwargs):
        return self.MANAGER

    @admin_access_granted
    def validate_current_user(self, *args, **kwargs) -> UserModel:
        """Override this method for custom user validation."""
        current_user = auth.current_user()
        self.check_roles(current_user, *args, **kwargs)
        self.check_permissions(current_user, args, **kwargs)
        return current_user

    def check_roles(self, current_user, *args, **kwargs):
        allowed_roles = self.get_allowed_roles()
        if allowed_roles is None:
            return
        if any(role for role in current_user.roles if role in allowed_roles):
            return
        raise Forbidden(FORBIDDEN)

    def check_permissions(self, current_user, *args, **kwargs):
        return

    def serialize_obj(self, instances, schema=None):
        schema = schema or self.get_schema_out()
        return schema(many=isinstance(instances, list)).dump(instances)

    def is_admins_allowed(self):
        return self.ALL_ADMINS_ALLOWED

    def get_allowed_roles(self):
        return self.ALLOWED_ROLES

    def create_login_response(self, token, user_data):
        user_type = user_data.__class__.__name__.lower().replace("model", "")
        user = self.serialize_obj(user_data)
        return {"token": token,
                "user_type": user_type,
                "user_data": user
                }
