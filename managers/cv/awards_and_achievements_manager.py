from managers.helpers.manager_mixins import CreateManagerMixin, GetManagerMixin
from models.cv.awards_and_achievements_model import AwardsAndAchievementsModel
from models.cv.reference_model import ReferenceModel


class AwardsAndAchievementsManager(CreateManagerMixin, GetManagerMixin):
    MODEL = AwardsAndAchievementsModel
