from managers.auth_manager import auth
from managers.cv.education_manager import EducationManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin
from schemas.request.cv.education_schema_in import EducationSchemaIn
from schemas.response.cv.education_schema_out import EducationSchemaOut


class CreateEducationResource(CreateResourceMixin):
    MANAGER = EducationManager
    SCHEMA_IN = EducationSchemaIn
    SCHEMA_OUT = EducationSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)


class EducationResource(GetResourceMixin):
    MANAGER = EducationManager
    SCHEMA_OUT = EducationSchemaOut

    @auth.login_required
    def get(self, user_id, education_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=education_id, **kwargs)
