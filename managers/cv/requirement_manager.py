from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, \
    DeleteManagerMixin
from models.cv.requirement_model import RequirementModel


class RequirementManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = RequirementModel
