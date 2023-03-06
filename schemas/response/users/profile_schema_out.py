from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.user.profile_model import ProfileFieldsEnum


class ProfileSchemaOut(Schema):
    class Meta:
        ordered = True

    first_name = fields.Str()

    last_name = fields.Str()

    date_of_birth = fields.Str()

    city = fields.Str()

    address = fields.Str()

    phone_number = fields.Str()

    profile_picture_file_url = fields.Str()

    public_fields = fields.List(EnumField(ProfileFieldsEnum,
                                          by_name=True)
                                )


class PublicProfileSchemaOut(Schema):
    class Meta:
        ordered = True

    first_name = fields.Str(attribute="public_first_name")

    last_name = fields.Str(attribute="public_last_name")

    date_of_birth = fields.Str(attribute="public_date_of_birth")

    city = fields.Str(attribute="public_city")

    address = fields.Str(attribute="public_address")

    phone_number = fields.Str(attribute="public_phone_number")

    profile_picture_file_url = fields.Str(attribute="public_profile_picture_file_url")
