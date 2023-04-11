from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.requirement_model import RequirementModel


class RequirementManager(CreateManagerMixin, GetManagerMixin):
    MODEL = RequirementModel
