from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.reference_model import ReferenceModel


class ReferenceManager(CreateManagerMixin, GetManagerMixin):
    MODEL = ReferenceModel
