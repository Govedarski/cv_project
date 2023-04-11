from db import db

cv_work_exps_association = db.Table(
    'cv_work_exp_association',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('work_exp_id', db.Integer, db.ForeignKey('work_exp.id'))
)
