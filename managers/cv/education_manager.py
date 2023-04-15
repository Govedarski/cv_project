from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, EditManagerMixin, GetListManagerMixin, \
    DeleteManagerMixin
from models.cv.education_model import EducationModel


class EducationManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = EducationModel
