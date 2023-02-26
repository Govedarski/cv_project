from enum import Enum

from models.profile_model import ProfileModel
from resources.helpers.resource_mixins import BaseResource
from resources.user.auth_resources import RegisterUserResource, LoginUserResource
from resources.user.profile_resources import ProfileResource
from utils.CustomEnum import CustomEnum, StaticCustomEnum


class HomeResource(BaseResource):
    def get(self):
        a = ProfileModel
        return {"status": "available"}


class Route(CustomEnum):
    def __init__(self, resource_class: BaseResource, url: str):
        self.resource_class = resource_class
        self.url = url


class Routes(StaticCustomEnum):
    REGISTER_USER = Route(RegisterUserResource, "/user/register")  # POST
    LOGIN_USER = Route(LoginUserResource, "/user/login")  # POST
    # (UserResource, Endpoints.USER[0]) # GET, PUT, PATCH, DELETE
    PROFILE = Route(ProfileResource, "/user/<int:user_pk>/profile")  # GET, PUT, PATCH, DELETE

    # (LoginUserViaGoogleResource, "/users/customers/login/google"),  # POST
    # (AuthorizeUserViaGoogleResource, "/users/customers/authorize/google"),  # POST    #
    # (WebhookResource, "/webhook")
    # TEST_ROUTE = (HomeResource, "/")  # POST
