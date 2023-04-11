from db import db

cv_requirement_association = db.Table(
    'cv_requirement_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('requirement_id', db.Integer, db.ForeignKey('requirement.id'))
)
