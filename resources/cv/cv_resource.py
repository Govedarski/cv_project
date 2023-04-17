from managers.auth_manager import auth
from managers.cv.cv_manager import CVManager
from managers.cv.reference_manager import ReferenceManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    EditResourceMixin, DeleteResourceMixin
from schemas.request.cv.cv_schema_in import CVSchemaIn
from schemas.response.cv.cv_schema_out import CVSchemaOut


class CVResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = CVManager
    SCHEMA_IN = CVSchemaIn
    SCHEMA_OUT = CVSchemaOut

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


class CVDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = CVManager
    SCHEMA_IN = CVSchemaIn
    SCHEMA_OUT = CVSchemaOut

    @auth.login_required
    def get(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=cv_id, **kwargs)

    @auth.login_required
    def put(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=cv_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=cv_id, **kwargs)

