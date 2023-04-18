from marshmallow import Schema, fields, post_dump
from marshmallow_enum import EnumField

from managers.user.profile_manager import ProfileManager
from models.enums.cv.education_level_enum import EducationLevelEnum
from models.enums.cv.language_enum import LanguageEnum
from models.enums.cv.public_status_enum import PublicStatusEnum
from schemas.response.users.profile_schema_out import ProfileSchemaOut


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

    requirements = fields.Nested(
        'RequirementSchemaOut',
        attribute='requirements')


    public_status = fields.Enum(PublicStatusEnum,
                                by_value=True)

    @post_dump
    def calculate_work_exp_ids(self, data, **kwargs):
        work_exps = data.get('work_exps', [])
        work_exp_ids = [work_exp['id'] for work_exp in work_exps]
        data['work_exp_ids'] = work_exp_ids

        education = data.get('education', [])
        education_ids = [e['id'] for e in education]
        data['education_ids'] = education_ids

        certificates = data.get('certificates', [])
        certificate_ids = [c['id'] for c in certificates]
        data['certificate_ids'] = certificate_ids

        references = data.get('references', [])
        reference_ids = [r['id'] for r in references]
        data['reference_ids'] = reference_ids

        profile = ProfileManager().get(data.get('owner_id'))
        data['profile'] = ProfileSchemaOut(many=isinstance(profile, list)).dump(profile)

        requirements = data.get('requirements')
        if requirements:
            data['requirements_id'] = requirements.get('id')
        return data
