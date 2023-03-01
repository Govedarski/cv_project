from sqlalchemy.dialects.postgresql import ARRAY

from db import db
from models.enums.contact_method_enum import ContactMethods
from models.enums.user_roles_enum import JobSeekerRoles
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
