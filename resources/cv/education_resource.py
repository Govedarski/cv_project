from managers.auth_manager import auth
from managers.cv.education_manager import EducationManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    EditResourceMixin, DeleteResourceMixin
from schemas.request.cv.education_schema_in import EducationSchemaIn
from schemas.response.cv.education_schema_out import EducationSchemaOut


class EducationResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = EducationManager
    SCHEMA_IN = EducationSchemaIn
    SCHEMA_OUT = EducationSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)

    @auth.login_required
    def get(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(**kwargs)


class EducationDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = EducationManager
    SCHEMA_OUT = EducationSchemaOut

    @auth.login_required
    def get(self, user_id, education_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=education_id, **kwargs)

    @auth.login_required
    def put(self, user_id, education_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=education_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, education_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=education_id, **kwargs)



