from managers.auth_manager import auth
from managers.cv.cv_manager import CVManager
from resources.helpers.resource_mixins import CreateResourceMixin
from schemas.request.cv.cv_schema_in import CVSchemaIn
from schemas.response.cv.cv_schema_out import CVSchemaOut


class CVResource (CreateResourceMixin):
    MANAGER = CVManager
    SCHEMA_IN = CVSchemaIn
    SCHEMA_OUT = CVSchemaOut
    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)