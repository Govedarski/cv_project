from sqlalchemy.dialects.postgresql import ARRAY

from db import db
from models.association_tables.cv.cv_a_and_a_association import cv_awards_and_achievements_association
from models.association_tables.cv.cv_certificate_association import cv_certificate_association
from models.association_tables.cv.cv_education_association import cv_education_association
from models.association_tables.cv.cv_reference_association import cv_reference_association
from models.association_tables.cv.cv_requirement_association import cv_requirement_association
from models.association_tables.cv.cv_work_exp_association import cv_work_exps_association
from models.enums.cv.education_level_enum import EducationLevelEnum
from models.enums.cv.language_enum import LanguageEnum
from models.helpers.base_model import BaseModel


class CVModel(BaseModel):
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    name = db.Column(db.String(64))
    # certificates = db.relationship('Certificate', secondary='cv_certificate', backref='cvs')
    hobbies = db.Column(db.String(100))
    summary = db.Column(db.String(500))
    education_level = db.Column(db.Enum(EducationLevelEnum))
    standard_languages = db.Column(ARRAY(db.Enum(LanguageEnum)))
    other_languages = db.Column(db.ARRAY(db.String(64)))
    professional_skills = db.Column(db.ARRAY(db.String(64)))
    soft_skills = db.Column(db.ARRAY(db.String(64)))
    references = db.relationship('ReferenceModel',
                                 secondary=cv_reference_association,
                                 backref='cvs')

    awards_and_achievements = db.relationship('AwardsAndAchievementsModel',
                                              secondary=cv_awards_and_achievements_association,
                                              backref='cvs')

    education = db.relationship('EducationModel',
                                              secondary=cv_education_association,
                                              backref='cvs')

    work_exps = db.relationship('WorkExpModel',
                                secondary=cv_work_exps_association,
                                backref='cvs')

    certificates = db.relationship('CertificateModel',
                                secondary=cv_certificate_association,
                                backref='cvs')

    requirements = db.relationship('RequirementModel',
                                  secondary=cv_requirement_association,
                                  backref='cv')