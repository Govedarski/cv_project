import factory

from models.user_models import UserModel
from tests.factories.base_factory import BaseFactory


class UserFactory(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    username = factory.Faker('user_name')
    email = factory.Faker("email")
    password = factory.Faker("password")

    def __init__(self, **kwargs):
        self.id = kwargs.get("id") or self.id
        self.username = kwargs.get("username") or self.username
        self.email = kwargs.get("email") or self.email
        self.password = kwargs.get("password") or self.password
