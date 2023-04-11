from marshmallow import Schema, fields, validate


class CertificateSchemaIn(Schema):
    name = fields.Str(required=True, validate=validate.Length(max=64))
    description = fields.Str(allow_none=True, validate=validate.Length(max=500))
    image_binary = fields.Str(allow_none=True)
    image_extension = fields.Str(allow_none=True)
    date = fields.Str(required=True)
