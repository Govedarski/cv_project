from flask_testing import TestCase

from config import create_app
from db import db
from managers.auth_manager import AuthManager
from tests.test_helpers.constants.configuration import TEST_CONFIGURATION


class BaseTestCase(TestCase):
    _HEADER_CONT_TYPE_JSON = {"Content-Type": "application/json"}

    def create_app(self):
        app = create_app(TEST_CONFIGURATION)

        @app.after_request
        def return_response(response):
            db.session.commit()
            return response

        return app

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def _assert_count_equal(count, model):
        assert len(model.query.all()) == count

    # @staticmethod
    # def _generate_token(user):
    #     token = AuthManager.encode_token(user)
    #     return token

    @staticmethod
    def _decode_token(token):
        return AuthManager.decode_token(token)
