from db import db
from models.enums.cv.employment_type_enum import EmploymentTypeEnum
from models.helpers.base_model import BaseModel


class WorkExpModel(BaseModel):
    __tablename__ = 'work_exp'
    owner_id = db.Column(db.Integer,
                         db.ForeignKey('job_seeker.id'),
                         nullable=False)
    company_name = db.Column(db.String(64), nullable=False)
    job_title = db.Column(db.String(64), nullable=False)
    field_of_work = db.Column(db.String(64), nullable=False)
    employment_type = db.Column(db.Enum(EmploymentTypeEnum), nullable=False)
    description = db.Column(db.String(500))
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)

