from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, DeleteManagerMixin, EditManagerMixin, \
    GetListManagerMixin
from models.cv.certificate_model import CertificateModel


class CertificateManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = CertificateModel


    def delete_image(self, _id):
        instance = self._get_instance(_id)
        instance.image_file_url = None

        return instance