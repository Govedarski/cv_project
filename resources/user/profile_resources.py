from managers.user.profile_manager import ProfileManager
from resources.helpers.resource_mixins import GetResourceMixin
from schemas.request.users.profile_schema_in import ProfileSchemaIn
from schemas.response.users.profile_schema_out import ProfileSchemaOut


class ProfileResource(GetResourceMixin):
    MANAGER = ProfileManager
    SCHEMA_IN = ProfileSchemaIn
    SCHEMA_OUT = ProfileSchemaOut

    def get(self, user_id, **kwargs):
        return super().get(user_id, **kwargs)
    # def put(self):
    #     return super().put()
    #
    # def patch(self):
    #     #TODO: try to add patch as option for modifying
    #     return {}
    # def delete(self):
    #     return super().delete()
