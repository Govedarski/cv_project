from sqlalchemy.orm import Query

from db import db
from models.helpers.base_model import BaseModel
from models.helpers.model_mixins import CreatedModelMixin
from models.user.user_model import UserSubclass


class ProfileModel(UserSubclass):
    __tablename__ = 'profile'
    query: Query

    is_public = db.Column(db.Boolean,
                          nullable=False,
                          default=False,
                          server_default='false')

    first_name = db.Column(db.String(255))

    last_name = db.Column(db.String(255))

    data_of_birth = db.Column(db.String(10))

    # TODO: TO ADD FILE_MIXIN AND ANYTHING NEED FOR FILE PROCESSING WITH AWS S3
    profile_picture_file_url = db.Column(db.String(255))

    city = db.Column(db.String(255))

    address = db.Column(db.Text)

    phone_number = db.Column(db.String(9))
