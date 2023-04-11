from db import db

cv_certificate_association = db.Table(
    'cv_certificate_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('certificate_id', db.Integer, db.ForeignKey('certificate.id'))
)

