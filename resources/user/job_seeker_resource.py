from managers.auth_manager import auth
from managers.user.job_seeker_manager import JobSeekerManager
from resources.helpers.permision_functions import is_user_with_valid_id
from resources.helpers.resource_mixins import GetResourceMixin, EditResourceMixin, PromoteResourceMixin
from schemas.request.users.job_seeker_schema_in import JobSeekerSchemaIn
from schemas.response.users.job_seeker_schema_out import JobSeekerSchemaOut


class JobSeekerResource(PromoteResourceMixin, GetResourceMixin, EditResourceMixin):
    MANAGER = JobSeekerManager
    SCHEMA_IN = JobSeekerSchemaIn
    SCHEMA_OUT = JobSeekerSchemaOut

    def post(self, user_id):
        return super().post(user_id)

    @auth.login_required
    def get(self, user_id, *args, **kwargs):
        return super().get(user_id)

    @auth.login_required
    def put(self, user_id, **kwargs):
        return super().put(user_id, **kwargs)

    def check_permissions(self, current_user, *args, **kwargs):
        is_user_with_valid_id(current_user, **kwargs)
