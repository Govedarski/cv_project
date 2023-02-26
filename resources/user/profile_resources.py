from managers.auth_manager import auth
from managers.profile_manager import ProfileManager
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin
from schemas.request.users.profile_schema_in import ProfileSchemaIn
from schemas.response.users.profile_schema_out import ProfileSchemaOut


class ProfileResource(CreateResourceMixin):
    MANAGER = ProfileManager
    SCHEMA_IN = ProfileSchemaIn
    SCHEMA_OUT = ProfileSchemaOut

    # def get(self):
    #     return super().get()

    @auth.login_required
    def post(self, user_pk):
        return super().post()
    #
    # def put(self):
    #     return super().put()
    #
    # def patch(self):
    #     #TODO: try to add patch as option for modifying
    #     return {}
    # def delete(self):
    #     return super().delete()

