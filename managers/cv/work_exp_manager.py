from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.work_exp_model import WorkExpModel


class WorkExpManager(CreateManagerMixin, GetManagerMixin):
    MODEL = WorkExpModel
