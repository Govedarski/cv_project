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
                ERROR_MESSAGE = "is already taken!"
                db.session.rollback()
                errors = {}
                model = cls.get_model()
                unique_columns = [column.name for column in model.__table__.columns if column.unique]
                pattern = r'Key \(([^)]+)'
                error_column = re.findall(pattern, ex.orig.pgerror)[0]
                errors[error_column] = ERROR_MESSAGE
                error_column_index = unique_columns.index(error_column)
                columns_to_check = unique_columns[error_column_index + 1:]
                for column in columns_to_check:
                    column_value = data.get(column)
                    if not column_value:
                        continue
                    criteria = {column: column_value}
                    if model.query.filter_by(**criteria).first():
                        errors[column] = ERROR_MESSAGE
                raise BadRequest(errors)
            raise ex
        return result

    return wrapper

