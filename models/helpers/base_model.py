from sqlalchemy import func
from sqlalchemy.orm import Query

from db import db


class BaseModel(db.Model):
    __abstract__ = True
    query: Query

    id = db.Column(db.Integer, primary_key=True)

    created_on = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    last_changed = db.Column(db.DateTime, onupdate=func.now())