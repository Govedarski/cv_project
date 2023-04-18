from managers.auth_manager import auth
from managers.cv.cv_manager import CVManager
from managers.cv.reference_manager import ReferenceManager
from models.enums.cv.public_status_enum import PublicStatusEnum
from resources.helpers.resource_mixins import CreateResourceMixin, GetResourceMixin, GetListResourceMixin, \
    EditResourceMixin, DeleteResourceMixin
from schemas.request.cv.cv_schema_in import CVSchemaIn
from schemas.response.cv.cv_schema_out import CVSchemaOut


class CVResource(CreateResourceMixin, GetListResourceMixin):
    MANAGER = CVManager
    SCHEMA_IN = CVSchemaIn
    SCHEMA_OUT = CVSchemaOut

    @auth.login_required
    def post(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().post(**kwargs)

    @auth.login_required
    def get(self, user_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(**kwargs)

    def filter_by(self):
        return {'owner_id': self.get_valid_current_user().id}


class CVDetailsResource(GetResourceMixin, EditResourceMixin, DeleteResourceMixin):
    MANAGER = CVManager
    SCHEMA_IN = CVSchemaIn
    SCHEMA_OUT = CVSchemaOut

    @auth.login_optional
    def get(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().get(_id=cv_id, **kwargs)

    @auth.login_required
    def put(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().put(_id=cv_id, **kwargs)

    @auth.login_required
    def delete(self, user_id, cv_id, **kwargs):
        self.get_valid_current_user(_id=user_id)
        return super().delete(_id=cv_id, **kwargs)

class CVAllResource( GetListResourceMixin):
    MANAGER = CVManager
    SCHEMA_OUT = CVSchemaOut





    @auth.login_optional
    def get(self, **kwargs):
        obj_list = self.get_manager()().get_list(self.filter_by(), **kwargs)
        user = auth.current_user()
        if user:
            obj_list = [cv for cv in obj_list if cv.public_status != PublicStatusEnum.PRIVATE]
        return [self.get_schema_out(instance=instance)().dump(instance) for instance in obj_list if instance], 200

    def filter_by(self):
        if not auth.current_user():
            return {"public_status":"PUBLIC"}
        return {}



class PublicCVResource(GetResourceMixin):
    MANAGER = CVManager
    SCHEMA_OUT = CVSchemaOut

    @auth.login_optional
    def get(self, _id, **kwargs):
        self.get_valid_current_user(_id=_id)
        instances = self.get_manager()().get(_id, **kwargs)
        if instances.public_status == PublicStatusEnum.PUBLIC:
            return self.serialize_obj(instances, _id=_id, **kwargs), 200

        if instances.public_status == PublicStatusEnum.PROTECTED and auth.current_user():
            return self.serialize_obj(instances, _id=_id, **kwargs), 200

        return {}, 200