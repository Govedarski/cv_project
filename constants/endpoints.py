from constants import methods
from resources.routes import Routes
from utils.CustomEnum import StaticCustomEnum


class Endpoints(StaticCustomEnum):
    REGISTER_USER = (Routes.REGISTER.url, methods.POST)
    LOGIN_USER = (Routes.LOGIN_JOB_SEEKER.url, methods.POST)


    SHOW_USER = (Routes.TALENT.url, methods.GET)
    UPDATE_USER = (Routes.TALENT.url, methods.GET)