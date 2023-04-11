from marshmallow import Schema, fields

from constants.extensions import ValidExtension
from schemas.validators.common_validators import ValidateExtension


class AwardsAndAchievementsSchemaIn(Schema):
    name = fields.String(required=True)
    date = fields.String(required=True)
    description = fields.String(required=True)

    image_binary = fields.String(allow_none=True)

    image_extension = fields.String(
        allow_none=True,
        validate=ValidateExtension(ValidExtension.image).validate
    )