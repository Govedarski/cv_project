from constants import methods
from resources.routes import Routes
from utils.CustomEnum import StaticCustomEnum


class Endpoints(StaticCustomEnum):
    REGISTER_USER = (Routes.REGISTER_USER.url, methods.POST)
    LOGIN_USER = (Routes.LOGIN_USER.url, methods.POST)

    CREATE_PROFILE = (Routes.PROFILE.url, methods.POST)
    SHOW_PROFILE = (Routes.PROFILE.url, methods.GET)
    UPDATE_PROFILE = (Routes.PROFILE.url, methods.PUT)
    MODIFY_PROFILE = (Routes.PROFILE.url, methods.PATCH)
    DELETE_PROFILE = (Routes.PROFILE.url, methods.DELETE)
