from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, DeleteManagerMixin, EditManagerMixin, \
    GetListManagerMixin
from models.cv.certificate_model import CertificateModel


class CertificateManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = CertificateModel
