from db import db
from models.helpers.base_model import BaseModel


class CertificateModel(BaseModel):
    __tablename__ = 'certificate'
    owner_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500))
    image_file_url = db.Column(db.String(255))
    date = db.Column(db.String(10), nullable=False)