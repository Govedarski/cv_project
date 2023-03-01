from werkzeug.exceptions import Forbidden

from constants.strings import FORBIDDEN


def is_user_with_valid_id(current_user, _id):
    if not current_user.id == _id:
        raise Forbidden(FORBIDDEN)

