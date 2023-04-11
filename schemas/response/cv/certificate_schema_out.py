from marshmallow import fields, Schema


class CertificateSchemaOut(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    date = fields.Str()
    image_file_url = fields.Str()
