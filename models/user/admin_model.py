from db import db
from models.helpers.model_mixins import CreatedModelMixin
from models.user.user_model import UserModel, UserSubclass


@UserModel.add_subclass()
class AdminModel(UserSubclass):
    __tablename__ = 'admin'

    # Todo add admin roles

    admin_password = db.Column(db.String(255), nullable=False)
