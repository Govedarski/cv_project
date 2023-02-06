import re

from psycopg2.errorcodes import UNIQUE_VIOLATION
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from db import db



def handle_unique_constrain_violation(func):
    def wrapper(cls, data, *args, **kwargs):
        try:
            result = func(cls, data, *args, **kwargs)
        except IntegrityError as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                db.session.rollback()
                errors = {}
                error_message = "Is already taken!"
                model = cls.get_model()
                unique_columns = [column.name for column in model.__table__.columns if column.unique]
                error_column = re.findall(r'Key \(([^)]+)', ex.orig.pgerror)[0]
                errors[error_column] = error_message
                error_column_index = unique_columns.index(error_column)
                columns_to_check = unique_columns[error_column_index + 1:]
                for column in columns_to_check:
                    criteria = {column: data[column]}
                    if model.query.filter_by(**criteria).first():
                        errors[column] = error_message
                raise BadRequest(errors)
            raise ex
        return result

    return wrapper



