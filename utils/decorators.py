import re

from psycopg2.errorcodes import UNIQUE_VIOLATION
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from db import db


def handle_unique_constrain_violation(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except IntegrityError as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                db.session.rollback()
                error = modify_error_message(ex.orig.pgerror)
                raise BadRequest(error)
            raise ex
        return result

    return wrapper


def modify_error_message(error_message):
    field, value = re.findall("\(([^\)]+)\)", error_message)
    return f"{field.capitalize()}: {value} is already taken!"
