from managers.auth_manager import auth
from managers.cv.awards_and_achievements_manager import AwardsAndAchievementsManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin
from schemas.request.cv.awards_and_achievements_schema_in import AwardsAndAchievementsSchemaIn
from schemas.response.cv.awards_and_achievements_schema_out import AwardsAndAchievementsSchemaOut


class CreateAwardsAndAchievementsResource(CreateResourceMixin):
    MANAGER = AwardsAndAchievementsManager
    SCHEMA_IN = AwardsAndAchievementsSchemaIn
    SCHEMA_OUT = AwardsAndAchievementsSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)


class AwardsAndAchievementsResource(GetResourceMixin):
    MANAGER = AwardsAndAchievementsManager
    SCHEMA_OUT = AwardsAndAchievementsSchemaOut

    @auth.login_required
    def get(self, user_id, aaa_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=aaa_id, **kwargs)
