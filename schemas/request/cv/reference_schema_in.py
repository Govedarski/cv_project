from marshmallow import Schema, fields, validate



class ReferenceSchemaIn(Schema):
    name = fields.Str(validate=validate.Length(min=3, max=64))

    position = fields.Str(validate=validate.Length(min=3, max=64))

    company = fields.Str(validate=validate.Length(min=3, max=64))

    contacts = fields.Str(validate=validate.Length(min=3, max=64))