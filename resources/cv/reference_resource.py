from managers.auth_manager import auth
from managers.cv.reference_manager import ReferenceManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    EditResourceMixin, DeleteResourceMixin
from schemas.request.cv.reference_schema_in import ReferenceSchemaIn
from schemas.response.cv.reference_schema_out import ReferenceSchemaOut


class ReferencesResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = ReferenceManager
    SCHEMA_IN = ReferenceSchemaIn
    SCHEMA_OUT = ReferenceSchemaOut

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

class ReferencesDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = ReferenceManager
    SCHEMA_IN = ReferenceSchemaIn
    SCHEMA_OUT = ReferenceSchemaOut

    @auth.login_required
    def get(self, user_id, reference_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=reference_id, **kwargs)

    @auth.login_required
    def put(self, user_id, reference_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=reference_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, reference_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=reference_id, **kwargs)