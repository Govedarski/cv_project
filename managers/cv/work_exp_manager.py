from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, \
    DeleteManagerMixin
from models.cv.work_exp_model import WorkExpModel


class WorkExpManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
    MODEL = WorkExpModel
