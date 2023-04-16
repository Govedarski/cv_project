from resources.cv.awards_and_achievements_resource import CreateAwardsAndAchievementsResource, \
    AwardsAndAchievementsResource
from resources.cv.certificate_resource import CreateCertificateResource, CertificateResource
from resources.cv.cv_resource import CVResource, CVDetailsResource
from resources.cv.education_resource import EducationResource, EducationDetailsResource
from resources.cv.reference_resource import ReferencesDetailsResource, ReferencesResource
from resources.cv.requirement_resource import RequirementsResource, RequirementsDetailsResource
from resources.cv.work_exp_resource import WorkExpResource, WorkExpDetailsResource
from resources.helpers.resource_mixins import BaseResource
from resources.user.auth_resources import RegisterResource, LoginJobSeekerResource, LoginEmployerResource, \
    LoginUserResource, ChangePasswordResource, RegisterJobSeeker
from resources.user.employer_resource import EmployerResource
# from resources.user.profile_resources import ProfileResource
from resources.user.job_seeker_resource import JobSeekerResource
from resources.user.profile_resources import ProfileResource, ProfilePictureResource
from resources.user.user_resource import UserResource
from utils.CustomEnum import CustomEnum, StaticCustomEnum
from models.user.job_seeker_model import JobSeekerModel
from models.user.employer_model import EmployerModel
from models.user.admin_model import AdminModel


class HomeResource(BaseResource):
    def get(self):
        return {"status": "available"}


class Route(CustomEnum):
    def __init__(self, resource_class: BaseResource, url: str):
        self.resource_class = resource_class
        self.url = url


# Todo: create admin part, add delete option for user and its profiles
class Routes(StaticCustomEnum):
    Home = Route(HomeResource, "/")
    REGISTER = Route(RegisterResource, "/user/register")  # POST
    REGISTER_JOB_SEEKER = Route(RegisterJobSeeker, "/user/register/job_seeker")  # POST
    LOGIN_USER = Route(LoginUserResource, "/user/login")  # POST
    LOGIN_JOB_SEEKER = Route(LoginJobSeekerResource, "/user/login/job_seeker")  # POST
    LOGIN_EMPLOYER = Route(LoginEmployerResource, "/user/login/employer")  # POST
    CHANGE_PASSWORD = Route(ChangePasswordResource, "/user/<int:user_id>/change_password")  # PUT

    USER = Route(UserResource, "/user/<int:user_id>")  # GET, PUT
    JOB_SEEKER = Route(JobSeekerResource, "/user/<int:user_id>/job_seeker")  # POST, GET, PUT
    EMPLOYER = Route(EmployerResource, "/user/<int:user_id>/employer")  # POST, GET, PUT
    PROFILE = Route(ProfileResource, "/user/<int:user_id>/profile")  # GET, PUT
    PROFILE_PICTURE = Route(ProfilePictureResource, "/user/<int:user_id>/profile/profile_picture")  # Delete

    CV = Route(CVResource, "/user/<int:user_id>/cv")  # POST, GET
    CV_DETAILS = Route(CVDetailsResource, "/user/<int:user_id>/cv/<int:cv_id>")  # GET

    REFERENCES = Route(ReferencesResource, "/user/<int:user_id>/references")  # POST
    REFERENCES_DETAILS = Route(ReferencesDetailsResource, "/user/<int:user_id>/references/<int:reference_id>")  # GET

    CREATE_A_AND_A = Route(CreateAwardsAndAchievementsResource, "/user/<int:user_id>/awards_and_achievements")  # POST
    A_AND_A = Route(AwardsAndAchievementsResource, "/user/<int:user_id>/awards_and_achievements/<int:aaa_id>")  # GET

    CREATE_EDUCATION = Route(EducationResource, "/user/<int:user_id>/education")  # POST
    EDUCATION = Route(EducationDetailsResource, "/user/<int:user_id>/education/<int:education_id>")  # GET


    WORK_EXP = Route(WorkExpResource, "/user/<int:user_id>/work_exp")  # POST, GET
    WORK_EXP_DETAILS = Route(WorkExpDetailsResource, "/user/<int:user_id>/work_exp/<int:work_exp_id>")  # GET, EDIT, DELETE

    CREATE_CERTIFICATE = Route(CreateCertificateResource, "/user/<int:user_id>/certificate")  # POST
    CERTIFICATE = Route(CertificateResource, "/user/<int:user_id>/certificate/<int:certificate_id>")  # GET
    # PUT AND IMAGE

    REQUIREMENT = Route(RequirementsResource, "/user/<int:user_id>/requirements")  # POST
    REQUIREMENTS_DETAILS = Route(RequirementsDetailsResource, "/user/<int:user_id>/requirements/<int:requirement_id>")  # GET

    # TALENT = Route(TalentResource, "/talent/<int:talent_id>")  # GET, PUT, DELETE for users
    # USERS = Route(UsersResource, "/user")  # GET, PUT, DELETE for list of users for Admin
    # CHANGE_PASSWORD  = Route(ChangePasswordUserResource, "/user/<int:user_pk>/change_password") # PUT
    # PROFILE = Route(ProfileResource, "/user/<int:user_id>/profile")  # GET, PUT, DELETE
    # PROFILES = Route(ProfileResource, "/user/profile")  # GET, PUT, DELETE

    # (LoginUserViaGoogleResource, "/users/customers/login/google"),  # POST
    # (AuthorizeUserViaGoogleResource, "/users/customers/authorize/google"),  # POST    #
    # (WebhookResource, "/webhook")
    # TEST_ROUTE = (HomeResource, "/")  # POST
