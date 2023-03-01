from sqlalchemy import func
from sqlalchemy.orm import Query

from db import db
from models.helpers.model_mixins import CreatedModelMixin


class BaseModel(CreatedModelMixin):
    __abstract__ = True
    query: Query

    id = db.Column(db.Integer, primary_key=True)
