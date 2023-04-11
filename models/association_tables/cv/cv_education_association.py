from db import db

cv_education_association = db.Table(
    'cv_education_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('education_id', db.Integer, db.ForeignKey('education.id'))
)
