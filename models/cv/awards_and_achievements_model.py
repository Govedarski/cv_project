from db import db
from models.helpers.base_model import BaseModel


class AwardsAndAchievementsModel(BaseModel):
    __tablename__ = 'awards_and_achievements'
    owner_id = db.Column(db.Integer,
                         db.ForeignKey('job_seeker.id'),
                         nullable=False)
    image_file_url = db.Column(db.String(255))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
