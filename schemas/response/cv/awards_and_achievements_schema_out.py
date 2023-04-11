from marshmallow import Schema, fields, validate


class AwardsAndAchievementsSchemaOut(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    date = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(equal=10),
        ))
    image_file_url = fields.Str()