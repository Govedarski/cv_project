from marshmallow import Schema, fields, validate

from models.enums.cv.education_level_enum import EducationLevelEnum


class EducationSchemaIn(Schema):
    institution = fields.String(required=True,
                                validate=validate.Length(max=100))
    education_level = fields.Enum(EducationLevelEnum, required=True, by_value=True)
    qualification = fields.String(allow_none=True, validate=validate.Length(max=100))
    fields_of_study = fields.List(fields.Str(), allow_none=True)
    start_date = fields.String(required=True)
    end_date = fields.String(required=True)
    description = fields.String(allow_none=True, validate=validate.Length(max=500))
    diploma_number = fields.String(validate=validate.Length(max=100))
    diploma_binary = fields.String(allow_none=True)
    diploma_extension = fields.String(allow_none=True)
