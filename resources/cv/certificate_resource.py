from managers.auth_manager import auth
from managers.cv.certificate_manager import CertificateManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin
from schemas.request.cv.certificate_schema_in import CertificateSchemaIn
from schemas.response.cv.certificate_schema_out import CertificateSchemaOut


class CreateCertificateResource(CreateResourceMixin):
    MANAGER = CertificateManager
    SCHEMA_IN = CertificateSchemaIn
    SCHEMA_OUT = CertificateSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)


class CertificateResource(GetResourceMixin):
    MANAGER = CertificateManager
    SCHEMA_OUT = CertificateSchemaOut

    @auth.login_required
    def get(self, user_id, certificate_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=certificate_id, **kwargs)
