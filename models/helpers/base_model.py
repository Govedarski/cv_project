from sqlalchemy import func
from sqlalchemy.orm import Query

from constants.file_suffix import FILE_SUFFIX_IN_DB
from db import db


class BaseModel(db.Model):
    __abstract__ = True
    query: Query

    id = db.Column(db.Integer, primary_key=True)

    created_on = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    last_changed = db.Column(db.DateTime, onupdate=func.now())

    is_deleted = db.Column(db.Boolean, default=False)

    @classmethod
    def get_all_file_field_names(cls):
        """Returns list of field names that has _file_url suffix and remove the suffix.
        Example:
        class A:
            x_file_url = ...
        A.get_all_file_field_names() -> "x"
        """
        return [x[0:-len(FILE_SUFFIX_IN_DB)]
                for x in cls.__dict__.keys()
                if x.endswith(FILE_SUFFIX_IN_DB)]
