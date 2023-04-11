from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.certificate_model import CertificateModel


class CertificateManager(CreateManagerMixin, GetManagerMixin):
    MODEL = CertificateModel
