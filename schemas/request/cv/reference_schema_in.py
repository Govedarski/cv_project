from marshmallow import Schema, fields, validate



class ReferenceSchemaIn(Schema):
    name = fields.Str(required=True, validate=validate.Length(max=100))

    position = fields.Str(required=True, validate=validate.Length(max=100))

    company = fields.Str(required=True, validate=validate.Length(max=100))

    contacts = fields.Str(required=True, validate=validate.Length(max=200))