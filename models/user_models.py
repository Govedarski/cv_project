from sqlalchemy.orm import Query

from db import db
from models.base_model import BaseModel


class BaseUserModel(BaseModel):
    __abstract__ = True

    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)


class UserModel(BaseUserModel):
    __tablename__ = 'user'
    query: Query

    profile = db.relationship("ProfileModel",
                              backref='user',
                              uselist=False)

    #Todo: to add roles
    is_admin = db.Column(db.Boolean, default=False)

