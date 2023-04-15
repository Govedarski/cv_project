from marshmallow import Schema, fields

from models.enums.cv.employment_type_enum import EmploymentTypeEnum


class WorkExpSchemaOut(Schema):
    id = fields.Int()
    company_name = fields.String()
    job_title = fields.String()
    field_of_work = fields.String()
    description = fields.String()
    employment_type = fields.Enum(EmploymentTypeEnum,
                                  by_value=True)
    start_date = fields.String()
    end_date = fields.String()

