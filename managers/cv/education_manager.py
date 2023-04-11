from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.education_model import EducationModel


class EducationManager(CreateManagerMixin, GetManagerMixin):
    MODEL = EducationModel
