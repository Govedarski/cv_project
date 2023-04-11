from db import db

cv_reference_association = db.Table(
    'cv_reference_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('reference_id', db.Integer, db.ForeignKey('reference.id'))
)
