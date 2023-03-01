from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.user_roles_enum import EmployerRoles
from schemas.response.users.profile_schema_out import ProfileSchemaOut
from schemas.response.users.user_schema_out import UserSchemaOut


class EmployerSchemaOut(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(required=True)

    roles = fields.List(EnumField(EmployerRoles,
                                  required=True,
                                  by_name=True))

    user = fields.Nested(UserSchemaOut)

    profile = fields.Nested(ProfileSchemaOut, attribute='user.profile')
