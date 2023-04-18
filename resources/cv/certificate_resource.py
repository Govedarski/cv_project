from managers.auth_manager import auth
from managers.cv.certificate_manager import CertificateManager
from resources.helpers.base_resource import BaseResource
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    DeleteResourceMixin, EditResourceMixin
from schemas.request.cv.certificate_schema_in import CertificateSchemaIn
from schemas.response.cv.certificate_schema_out import CertificateSchemaOut


class CertificateResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = CertificateManager
    SCHEMA_IN = CertificateSchemaIn
    SCHEMA_OUT = CertificateSchemaOut

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

class CertificateDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = CertificateManager
    SCHEMA_IN = CertificateSchemaIn
    SCHEMA_OUT = CertificateSchemaOut
    REMOVE_IMAGES_ON_EDIT = True

    @auth.login_required
    def get(self, user_id, certificate_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=certificate_id, **kwargs)

    @auth.login_required
    def put(self, user_id, certificate_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=certificate_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, certificate_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=certificate_id, **kwargs)

class CertificateImageResource(BaseResource):
    MANAGER = CertificateManager
    SCHEMA_OUT = CertificateSchemaOut

    @auth.login_required
    def delete(self, user_id, certificate_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        self.get_manager()().delete_image(_id=certificate_id)
        return {}, 200
