from marshmallow import fields, Schema, validate, post_load
from werkzeug.security import generate_password_hash

from schemas.request.users.profile_schema_in import ProfileSchemaIn
from schemas.validators.common_validators import ValidateIsAlphaNumericAndSpace
from schemas.validators.password_validator import PasswordValidator


class RegisterSchemaIn(ProfileSchemaIn):
    email = fields.Email(required=True)

    username = fields.Str(validate=validate.And(
        validate.Length(min=3, max=64),
        ValidateIsAlphaNumericAndSpace().validate
    ))

    password = fields.Str(required=True,
                          validate=PasswordValidator().validate_password)

    @post_load
    def hash_password(self, data, *args, **kwargs):
        data["password"] = generate_password_hash(data["password"])
        return data


class LoginSchemaIn(Schema):
    identifier = fields.Str(required=True)

    password = fields.Str(required=True)
