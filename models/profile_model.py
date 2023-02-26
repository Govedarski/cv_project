from sqlalchemy.orm import Query

from db import db
from models.base_model import BaseModel
from models.enums.contact_method_enum import ContactMethods


class ProfileModel(BaseModel):
    __tablename__ = 'profile'
    query: Query

    id = db.Column(db.Integer,
                   primary_key=True)

    creator_id = db.Column(db.Integer,
                           db.ForeignKey("user.id"),
                           nullable=False,
                           unique=True)

    first_name = db.Column(db.String(255))

    last_name = db.Column(db.String(255))

    data_of_birth = db.Column(db.String(10))

    # TODO: TO ADD FILE_MIXIN AND ANYTHING NEED FOR FILE PROCESSING WITH AWS S3
    profile_picture_file_url = db.Column(db.String(255))

    city = db.Column(db.String(255))

    address = db.Column(db.Text)

    phone_number = db.Column(db.String(9))

    preferred_contact_method = db.Column(db.Enum(ContactMethods),
                                         default=ContactMethods.any,
                                         nullable=False)

    # TODO: Add requirements, cvs, motivation latter templates
