from sqlalchemy.orm import declared_attr

from db import db
from models.helpers.base_model import BaseModel
from models.helpers.model_mixins import CreatedModelMixin


class UserModel(BaseModel):
    __tablename__ = 'user'
    _subclasses = {}

    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)

    profile = db.relationship('ProfileModel',
                              backref='user',
                              uselist=False)

    job_seeker = db.relationship('JobSeekerModel',
                                 backref='user',
                                 uselist=False)

    employer = db.relationship('EmployerModel',
                               backref='user',
                               uselist=False)

    admin = db.relationship('AdminModel',
                            backref='user',
                            uselist=False)

    @classmethod
    def add_subclass(cls):
        def decorator(subclass):
            cls._subclasses[subclass.__name__] = subclass
            return subclass

        return decorator

    @classmethod
    def get_usermodel(cls, name):
        if name == cls.__name__:
            return cls

        return cls._subclasses.get(name)


class UserSubclass(CreatedModelMixin):
    __abstract__ = True

    @declared_attr
    def id(cls):
        return db.Column(
            db.Integer,
            db.ForeignKey("user.id"),
            primary_key=True,
            nullable=False,
            unique=True)

