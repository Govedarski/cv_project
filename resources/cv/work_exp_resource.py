from managers.auth_manager import auth
from managers.cv.work_exp_manager import WorkExpManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    EditResourceMixin, DeleteResourceMixin
from schemas.request.cv.work_exp_schema_in import WorkExpSchemaIn
from schemas.response.cv.work_exp_schema_out import WorkExpSchemaOut


class WorkExpResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = WorkExpManager
    SCHEMA_IN = WorkExpSchemaIn
    SCHEMA_OUT = WorkExpSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)

    @auth.login_required
    def get(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(**kwargs)

    def filter_by(self):
        return {'owner_id': self.get_valid_current_user().id}

class WorkExpDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = WorkExpManager
    SCHEMA_IN = WorkExpSchemaIn
    SCHEMA_OUT = WorkExpSchemaOut

    @auth.login_required
    def get(self, user_id, work_exp_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=work_exp_id, **kwargs)

    @auth.login_required
    def put(self, user_id, work_exp_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=work_exp_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, work_exp_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=work_exp_id, **kwargs)