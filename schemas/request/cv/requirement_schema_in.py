from marshmallow import Schema, fields

from models.enums.cv.employment_type_enum import EmploymentTypeEnum


class RequirementSchemaIn(Schema):
    name = fields.String(required=True)
    salary_min_range = fields.Integer(allow_none=True)
    salary_max_range = fields.Integer(allow_none=True)
    employment_type = fields.Enum(EmploymentTypeEnum,
                                  by_value=True)



