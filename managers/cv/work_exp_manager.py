from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin, GetListManagerMixin
from models.cv.work_exp_model import WorkExpModel


class WorkExpManager(CreateManagerMixin, GetManagerMixin, GetListManagerMixin):
    MODEL = WorkExpModel
