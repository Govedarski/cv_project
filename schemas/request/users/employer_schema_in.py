from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.user_roles_enum import EmployerRoles


class EmployerSchemaIn(Schema):
    roles = fields.List(EnumField(EmployerRoles,
                                  error_messages={'by_name': "Invalid role"}))
