from marshmallow import Schema, fields, validate

from models.enums.cv.employment_type_enum import EmploymentTypeEnum


class WorkExpSchemaIn(Schema):
    company_name = fields.String(required=True, validate=validate.Length(max=64))
    job_title = fields.String(required=True, validate=validate.Length(max=64))
    field_of_work = fields.String(required=True, validate=validate.Length(max=64))
    description = fields.String(validate=validate.Length(max=500))
    employment_type = fields.Enum(EmploymentTypeEnum, required=True, by_value=True)
    start_date = fields.String(required=True)
    end_date = fields.String(required=True)