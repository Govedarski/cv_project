from marshmallow import Schema, fields

from schemas.response.users.profile_schema_out import ProfileSchemaOut


class UserSchemaOut(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(required=True)

    email = fields.Str(required=True)

    username = fields.Str(required=True)


class ExtendUserSchemaOut(UserSchemaOut):
    class Meta:
        ordered = True

    profile = fields.Nested(ProfileSchemaOut)

    has_job_seeker_profile = fields.Boolean(attribute="job_seeker")

    has_employer_profile = fields.Boolean(attribute="employer")
