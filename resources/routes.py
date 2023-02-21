from resources.helpers.resources_mixins import BaseResource
from resources.user.auth_resources import RegisterUserResource, LoginUserResource
from constants.endpoints import Endpoints


class HomeResource(BaseResource):
    def get(self):
        return {"status":"available"}

routes = (
    (HomeResource, "/"),  # POST
    (RegisterUserResource, Endpoints.REGISTER_USER[0]),  # POST
    (LoginUserResource, Endpoints.LOGIN_USER[0]),  # POST
    # (LoginUserViaGoogleResource, "/users/customers/login/google"),  # POST
    # (AuthorizeUserViaGoogleResource, "/users/customers/authorize/google"),  # POST    #
    # (WebhookResource, "/webhook")
)

