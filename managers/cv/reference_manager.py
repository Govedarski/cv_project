from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, DeleteManagerMixin, EditManagerMixin, \
    GetListManagerMixin
from models.cv.reference_model import ReferenceModel


class ReferenceManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = ReferenceModel
