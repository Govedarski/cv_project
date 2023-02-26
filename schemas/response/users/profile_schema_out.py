from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.contact_method_enum import ContactMethods


class ProfileSchemaOut(Schema):
    id = fields.Integer(required=True)

    creator_id = fields.Integer(required=True)

    first_name = fields.Str()

    last_name = fields.Str()

    city = fields.Str()
    address = fields.Str()

    phone_number = fields.Str()

    preferred_contact_method = EnumField(ContactMethods,
                                         required=True,
                                         by_name=True)

    profile_picture_binary = fields.Str()
