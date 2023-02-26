from marshmallow import Schema, fields

from schemas.response.users.profile_schema_out import ProfileSchemaOut


class UserSchemaOut(Schema):
    id = fields.Integer(required=True)

    email = fields.Str(required=True)

    username = fields.Str(required=True)

    profile = fields.Nested(ProfileSchemaOut)

    class Meta:
        ordered = True
