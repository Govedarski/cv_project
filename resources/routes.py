from resources.helpers.resource_mixins import BaseResource
from resources.user.auth_resources import RegisterResource, LoginJobSeekerResource, LoginEmployerResource, \
    LoginUserResource, ChangePasswordResource
from resources.user.employer_resource import EmployerResource
# from resources.user.profile_resources import ProfileResource
from resources.user.job_seeker_resource import JobSeekerResource
from resources.user.profile_resources import ProfileResource
from resources.user.user_resource import UserResource
from utils.CustomEnum import CustomEnum, StaticCustomEnum
from models.user.job_seeker_model import JobSeekerModel
from models.user.employer_model import EmployerModel
from models.user.admin_model import AdminModel


# class HomeResource(BaseResource):
#     # def get(self):
#     #     a = ProfileModel
#     #     return {"status": "available"}
#

class Route(CustomEnum):
    def __init__(self, resource_class: BaseResource, url: str):
        self.resource_class = resource_class
        self.url = url


# Todo: create admin part, add delete option for user and its profiles
class Routes(StaticCustomEnum):
    REGISTER = Route(RegisterResource, "/user/register")  # POST
    LOGIN_USER = Route(LoginUserResource, "/user/login")  # POST
    LOGIN_JOB_SEEKER = Route(LoginJobSeekerResource, "/user/login/job_seeker")  # POST
    LOGIN_EMPLOYER = Route(LoginEmployerResource, "/user/login/employer")  # POST
    CHANGE_PASSWORD = Route(ChangePasswordResource, "/user/<int:user_id>/change_password")  # PUT

    USER = Route(UserResource, "/user/<int:user_id>")  # GET, PUT
    JOB_SEEKER = Route(JobSeekerResource, "/user/<int:user_id>/job_seeker")  # POST, GET, PUT
    EMPLOYER = Route(EmployerResource, "/user/<int:user_id>/employer")  # POST, GET, PUT
    PROFILE = Route(ProfileResource, "/user/<int:user_id>/profile") # GET, PUT
    # PUT AND IMAGE

    # TALENT = Route(TalentResource, "/talent/<int:talent_id>")  # GET, PUT, DELETE for users
    # USERS = Route(UsersResource, "/user")  # GET, PUT, DELETE for list of users for Admin
    # CHANGE_PASSWORD  = Route(ChangePasswordUserResource, "/user/<int:user_pk>/change_password") # PUT
    # PROFILE = Route(ProfileResource, "/user/<int:user_id>/profile")  # GET, PUT, DELETE
    # PROFILES = Route(ProfileResource, "/user/profile")  # GET, PUT, DELETE

    # (LoginUserViaGoogleResource, "/users/customers/login/google"),  # POST
    # (AuthorizeUserViaGoogleResource, "/users/customers/authorize/google"),  # POST    #
    # (WebhookResource, "/webhook")
    # TEST_ROUTE = (HomeResource, "/")  # POST
