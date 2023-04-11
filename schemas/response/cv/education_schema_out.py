from marshmallow import Schema, fields

from models.enums.cv.education_level_enum import EducationLevelEnum


class EducationSchemaOut(Schema):
    id = fields.Integer()
    institution = fields.String()
    education_level = fields.Enum(EducationLevelEnum, by_value=True)
    qualification = fields.String()
    fields_of_study = fields.List(fields.Str())
    start_date = fields.String()
    end_date = fields.String()
    description = fields.String()
    diploma_number = fields.String()
    diploma_file_url = fields.String()
    owner_id = fields.Integer()