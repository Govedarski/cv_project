import base64
import uuid


from werkzeug.exceptions import BadRequest, NotFound

from constants.strings import PAGE_NOT_FOUND


def get_or_404(model, pk, message=None):
    if not message:
        message = PAGE_NOT_FOUND

    instance = model.query.filter_by(id=pk).first()
    if not instance or instance.is_deleted:
        raise NotFound(message)
    return instance


def decode_file(encoded_file):
    return base64.b64decode(encoded_file.encode("utf-8"))


def save_file(path, file):
    with open(path, "wb") as f:
        f.write(file)


def create_file(photo_str, extension):
    file_name = f"{str(uuid.uuid4())}.{extension}"
    return file_name, decode_file(photo_str)


def has_file_data(photo_str, extension):
    if not photo_str and extension:
        raise BadRequest("There is not photo provided!")
    elif photo_str and not extension:
        raise BadRequest("There is not extension provided!")
    elif not photo_str and not extension:
        return False
    return True


def get_file_name_by_url(photo_url):
    try:
        return photo_url.split("/")[-1]
    except AttributeError:
        return None

