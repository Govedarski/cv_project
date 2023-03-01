from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.contact_method_enum import ContactMethods


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


