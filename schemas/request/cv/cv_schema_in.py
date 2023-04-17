from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models.enums.cv.education_level_enum import EducationLevelEnum
from models.enums.cv.language_enum import LanguageEnum
from models.enums.cv.public_status_enum import PublicStatusEnum
from schemas.validators.common_validators import ValidateIsAlphaNumericAndSpace


class CVSchemaIn(Schema):
    name=fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=3, max=64),
            ValidateIsAlphaNumericAndSpace().validate
        ))

    hobbies = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=3, max=64),
            ValidateIsAlphaNumericAndSpace().validate
        ))

    summary = fields.Str(
        allow_none=True,
        validate=validate.And(
            validate.Length(min=3, max=64),
            ValidateIsAlphaNumericAndSpace().validate
        ))

    education_level = EnumField(
        EducationLevelEnum,
        allow_none=True,
        by_name=True)

    standard_languages = fields.List(
        EnumField(
            LanguageEnum,
            allow_none=True,
            by_name=True),
        allow_none=True)

    other_languages = fields.List(
        fields.Str(),
        allow_none=True)

    professional_skills = fields.List(
        fields.Str(),
        allow_none=True)

    soft_skills = fields.List(
        fields.Str(),
        allow_none=True)

    reference_ids = fields.List(fields.Integer(), allow_none=True)

    aaa_ids = fields.List(fields.Integer(), allow_none=True)
    education_ids = fields.List(fields.Integer(), allow_none=True)
    work_exp_ids = fields.List(fields.Integer(), allow_none=True)
    certificate_ids = fields.List(fields.Integer(), allow_none=True)
    requirements_id = fields.Integer(allow_none=True)

    public_status = EnumField(
        PublicStatusEnum,
        allow_none=True,
        by_value=True)