from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.cv.education_level_enum import EducationLevelEnum
from models.enums.cv.language_enum import LanguageEnum


class CVSchemaOut(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(required=True)

    name = fields.String()

    owner_id = fields.Integer(required=True)

    hobbies = fields.String()

    summary = fields.String()

    education_level = EnumField(EducationLevelEnum,
                                by_name=True)

    standard_languages = fields.List(
        EnumField(
            LanguageEnum,
            by_name=True)
    )

    other_languages = fields.List(fields.String())

    professional_skills = fields.List(fields.String())

    soft_skills = fields.List(fields.String())

    references = fields.List(
        fields.Nested(
            'ReferenceSchemaOut',
            attribute='references')
    )
    awards_and_achievements = fields.List(
        fields.Nested(
            'AwardsAndAchievementsSchemaOut',
            attribute='awards_and_achievements')
    )

    education = fields.List(
        fields.Nested(
            'EducationSchemaOut',
            attribute='education')
    )

    work_exps = fields.List(
        fields.Nested(
            'WorkExpSchemaOut',
            attribute='work_exps')
    )

    certificates = fields.List(
        fields.Nested(
            'CertificateSchemaOut',
            attribute='certificates')
    )

    requirements = fields.List(
        fields.Nested(
            'RequirementSchemaOut',
            attribute='requirements')
    )
