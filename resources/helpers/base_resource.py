from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from managers.auth_manager import auth
from managers.helpers.base_manager import BaseManager


class BaseResource(Resource):
    MANAGER = BaseManager
    SCHEMA_IN = None
    SCHEMA_OUT = None

    def get_data(self, *args, **kwargs):
        """Validation is happened here so if you need to override this always call super
        or validate the schema on your own."""
        schema = self.get_schema_in(*args, **kwargs)
        data = request.get_json() if request.data else None

        try:
            return schema(many=isinstance(data, list)).load(data) if data else None
        except ValidationError as ex:
            raise BadRequest(ex.messages)

    def get_schema_in(self, *args, **kwargs):
        return self.SCHEMA_IN

    def get_schema_out(self, *args, **kwargs):
        return self.SCHEMA_OUT

    def get_manager(self, *args, **kwargs):
        return self.MANAGER

    def get_user(self, *args, **kwargs):
        """Override this method for user validation as is he creator or has he permissions"""
        return auth.current_user()

    def serialize_obj(self, instances):
        return self.get_schema_out(instance=instances)(many=isinstance(instances, list)).dump(instances)