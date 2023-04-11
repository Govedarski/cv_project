from sqlalchemy.dialects.postgresql import ARRAY

from db import db
from models.enums.user.contact_method_enum import ContactMethods
from models.enums.user.user_roles_enum import JobSeekerRoles
from models.user.user_model import UserSubclass, UserModel


@UserModel.add_subclass()
class JobSeekerModel(UserSubclass):
    __tablename__ = 'job_seeker'

    preferred_contact_method = db.Column(db.Enum(ContactMethods),
                                         default=ContactMethods.any,
                                         nullable=False)

    roles = db.Column(ARRAY(db.Enum(JobSeekerRoles)),
                      default=[JobSeekerRoles.talent],
                      nullable=False)

    cvs = db.relationship('CVModel', backref='job_seeker')

    reference = db.relationship('ReferenceModel', backref='job_seeker')

    awards_and_achievements = db.relationship('AwardsAndAchievementsModel', backref='job_seeker')

    education = db.relationship('EducationModel', backref='job_seeker')

    work_exps = db.relationship('WorkExpModel', backref='job_seeker')

    certificates = db.relationship('CertificateModel', backref='job_seeker')

    requirements = db.relationship('RequirementModel', backref='job_seeker')