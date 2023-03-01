from enum import Enum

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Query

from db import db
from models.user.user_model import UserSubclass


class ProfileFieldsEnum(Enum):
    first_name = "profile name"
    last_name = "last name"
    data_of_birth = "data of birth"
    profile_picture_file_url = "profile picture"
    city = "city"
    address = "address"
    phone_number = "phone number"


class ProfileModel(UserSubclass):
    __tablename__ = 'profile'
    query: Query

    first_name = db.Column(db.String(255))

    last_name = db.Column(db.String(255))

    date_of_birth = db.Column(db.String(10))

    # TODO: TO ADD FILE_MIXIN AND ANYTHING NEED FOR FILE PROCESSING WITH AWS S3
    profile_picture_file_url = db.Column(db.String(255))

    city = db.Column(db.String(255))

    address = db.Column(db.Text)

    phone_number = db.Column(db.String(9))

    public_fields = db.Column(ARRAY(db.Enum(ProfileFieldsEnum)))


