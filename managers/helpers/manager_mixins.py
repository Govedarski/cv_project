from sqlalchemy.exc import InvalidRequestError

from managers.helpers.base_manager import BaseManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.image_manager import ImageManager


class CreateManagerMixin(BaseManager):
    @classmethod
    @handle_unique_constrain_violation
    def create(cls, data, user=None):
        if hasattr(cls.get_model(), "creator_id") and user:
            data["creator_id"] = user.id

        if cls.need_image_handler():
            return ImageManager.create_with_images(cls.get_model(), data)

        return cls.create_obj(cls.get_model(), data)


class GetManagerMixin(BaseManager):
    def get(self, filter_by):
        query = self.get_model().query
        for field, criteria in filter_by.items():
            if ".in" in field:
                field_name = field.split(".")[0]
                query = query.filter(getattr(self.get_model(), field_name).contains(criteria))
            else:
                current_criteria = {field: criteria}
                query = query.filter_by(**current_criteria)

        try:
            return query.all()
        except InvalidRequestError:
            # Invalid query string
            return []
