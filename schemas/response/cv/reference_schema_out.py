from marshmallow import Schema, fields


class ReferenceSchemaOut(Schema):
    id = fields.Integer(required=True)

    name = fields.Str()

    position = fields.Str()

    company = fields.Str()

    contacts = fields.Str()