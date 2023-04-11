from marshmallow import Schema, fields, validate

from models.enums.cv.education_level_enum import EducationLevelEnum


class EducationSchemaIn(Schema):
    institution = fields.String(required=True,
                                validate=validate.Length(max=100))
    education_level = fields.Enum(EducationLevelEnum, required=True, by_name=True)
    qualification = fields.String(allow_none=True, validate=validate.Length(max=100))
    fields_of_study = fields.List(fields.Str(), allow_none=True)
    start_date = fields.String(required=True)
    end_date = fields.String(allow_none=True, required=True)
    description = fields.String(required=True, validate=validate.Length(max=500))
    diploma_number = fields.String(required=True, validate=validate.Length(max=100))
    diploma_binary = fields.String(allow_none=True)
    diploma_extension = fields.String(allow_none=True)
