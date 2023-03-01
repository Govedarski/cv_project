from sqlalchemy.dialects.postgresql import ARRAY

from db import db
from models.enums.user_roles_enum import EmployerRoles
from models.helpers.model_mixins import CreatedModelMixin
from models.user.user_model import UserSubclass, UserModel


@UserModel.add_subclass()
class EmployerModel(UserSubclass):
    __tablename__ = 'employer'

    roles = db.Column(ARRAY(db.Enum(EmployerRoles)),
                      default=[EmployerRoles.recruiter],
                      nullable=False)

    # TODO: create jobs, invite to interview
