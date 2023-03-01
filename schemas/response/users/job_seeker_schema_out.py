from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.contact_method_enum import ContactMethods
from models.enums.user_roles_enum import JobSeekerRoles
from schemas.response.users.profile_schema_out import ProfileSchemaOut
from schemas.response.users.user_schema_out import UserSchemaOut


class JobSeekerSchemaOut(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(required=True)

    preferred_contact_method = EnumField(ContactMethods,
                                         required=True,
                                         by_name=True)

    roles = fields.List(EnumField(JobSeekerRoles,
                                  required=True,
                                  by_name=True))

    user = fields.Nested(UserSchemaOut)

    profile = fields.Nested(ProfileSchemaOut, attribute='user.profile')
