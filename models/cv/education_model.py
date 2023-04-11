from sqlalchemy.dialects.postgresql import ARRAY

from db import db
from models.enums.cv.education_level_enum import EducationLevelEnum
from models.helpers.base_model import BaseModel


class EducationModel(BaseModel):
    __tablename__ = 'education'
    owner_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)

    institution = db.Column(db.String(100), nullable=False)
    education_level = db.Column(db.Enum(EducationLevelEnum), nullable=False)
    qualification = db.Column(db.String(100), nullable=False)
    fields_of_study = db.Column(ARRAY(db.String(100)), nullable=False)
    start_date = db.Column(db.String(100), nullable=False)
    end_date = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    diploma_number = db.Column(db.String(100), nullable=False)
    diploma_file_url = db.Column(db.String(255), nullable=False)
