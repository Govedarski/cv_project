from db import db

cv_awards_and_achievements_association = db.Table(
    'cv_awards_and_achievements_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('cv_awards_and_achievements_id', db.Integer, db.ForeignKey('awards_and_achievements.id'))
)
