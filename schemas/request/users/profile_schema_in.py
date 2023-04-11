from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from constants.extensions import ValidExtension
from models.enums.user.contact_method_enum import ContactMethods
from models.user.profile_model import ProfileFieldsEnum
from schemas.validators.common_validators import ValidateIsAlphaAndSpace, ValidateExtension, ValidateIsNumeric


class ProfileSchemaIn(Schema):
    first_name = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=2, max=64),
            ValidateIsAlphaAndSpace().validate
        ))
    last_name = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=2, max=64),
            ValidateIsAlphaAndSpace().validate
        ))

    city = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=2, max=64),
            ValidateIsAlphaAndSpace().validate
        ))

    address = fields.Str(allow_none=True)

    # Todo: add dateformat validator
    date_of_birth = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(equal=10),
        ))

    phone_number = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(equal=13),
            ValidateIsNumeric().validate
        ))

    preferred_contact_method = EnumField(
        ContactMethods,
        error_messages={'by_name': "Invalid method"}
    )

    profile_picture_binary = fields.String(allow_none=True)

    profile_picture_extension = fields.String(
        allow_none=True,
        validate=ValidateExtension(ValidExtension.image).validate
    )

    public_fields = fields.List(
        EnumField(
            ProfileFieldsEnum,
            error_messages={'by_name': "Invalid field name"}
        )
    )
