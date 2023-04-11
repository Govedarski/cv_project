from db import db
from models.helpers.base_model import BaseModel


class ReferenceModel(BaseModel):
    __tablename__ = 'reference'
    owner_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    contacts = db.Column(db.String(200), nullable=False)