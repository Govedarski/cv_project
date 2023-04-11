from managers.auth_manager import auth
from managers.cv.requirement_manager import RequirementManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin
from schemas.request.cv.requirement_schema_in import RequirementSchemaIn
from schemas.response.cv.requirement_schema_out import RequirementSchemaOut


class CreateRequirementResource(CreateResourceMixin):
    MANAGER = RequirementManager
    SCHEMA_IN = RequirementSchemaIn
    SCHEMA_OUT = RequirementSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)


class RequirementResource(GetResourceMixin):
    MANAGER = RequirementManager
    SCHEMA_OUT = RequirementSchemaOut

    @auth.login_required
    def get(self, user_id, requirement_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=requirement_id, **kwargs)
