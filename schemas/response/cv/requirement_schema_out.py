from marshmallow import Schema, fields

from models.enums.cv.employment_type_enum import EmploymentTypeEnum


class RequirementSchemaOut(Schema):
    id = fields.Int()
    name = fields.Str()
    salary_min_range = fields.Int()
    salary_max_range = fields.Int()
    employment_type = fields.Enum(EmploymentTypeEnum, by_value=True)