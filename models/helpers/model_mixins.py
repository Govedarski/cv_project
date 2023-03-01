from sqlalchemy import func

from db import db


class CreatedModelMixin(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    last_changed = db.Column(db.DateTime, onupdate=func.now())
