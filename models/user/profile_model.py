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

    @property
    def public_first_name(self):
        return self.public_value_of("first_name")

    last_name = db.Column(db.String(255))

    @property
    def public_last_name(self):
        return self.public_value_of("last_name")

    date_of_birth = db.Column(db.String(10))

    @property
    def public_date_of_birth(self):
        return self.public_value_of("date_of_birth")

    # TODO: TO ADD FILE_MIXIN AND ANYTHING NEED FOR FILE PROCESSING WITH AWS S3
    profile_picture_file_url = db.Column(db.String(255))

    @property
    def public_profile_picture_file_url(self):
        return self.public_value_of("profile_picture_file_url")

    city = db.Column(db.String(255))

    @property
    def public_city(self):
        return self.public_value_of("city")

    address = db.Column(db.Text)

    @property
    def public_address(self):
        return self.public_value_of("address")

    phone_number = db.Column(db.String(9))

    @property
    def public_phone_number(self):
        return self.public_value_of("phone_number")

    public_fields = db.Column(ARRAY(db.Enum(ProfileFieldsEnum)))

    def public_value_of(self, field_name):
        if not self.public_fields:
            return None
        value = getattr(self, field_name)
        field_enum = getattr(ProfileFieldsEnum, field_name)
        return value if field_enum in self.public_fields else None
