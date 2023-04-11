from db import db
from models.enums.cv.employment_type_enum import EmploymentTypeEnum
from models.helpers.base_model import BaseModel


class RequirementModel(BaseModel):
    __tablename__ = 'requirement'
    owner_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    salary_min_range = db.Column(db.Integer)
    salary_max_range = db.Column(db.Integer)
    employment_type = db.Column(db.Enum(EmploymentTypeEnum))
