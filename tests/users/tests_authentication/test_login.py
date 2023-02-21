from werkzeug.security import generate_password_hash

from constants.endpoints import Endpoints
from managers.auth_manager import AuthManager
from managers.user_manager import UserManager
from tests.base_test_case import BaseTestCase
from tests.factories.user_factory import UserFactory


class TestLoginCustomer(BaseTestCase):
    URL = Endpoints.LOGIN_USER[0]
    VAlID_CREDENTIALS = {
        "username": "test",
        "email": "test@test.com",
        "password": "testP@ss1!",
    }
    SECOND_USER_CREDENTIALS = {
        "username": "second test",
        "email": "secondtest@test.com",
    }
    THIRD_USER_CREDENTIALS = {
        "username": "third test",
        "email": "thirdtest@test.com",
        "password": "testP@ss2!",
    }

    def setUp(self):
        super().setUp()
        self.user = UserFactory(username=self.VAlID_CREDENTIALS["username"],
                                email=self.VAlID_CREDENTIALS["email"],
                                password=generate_password_hash(self.VAlID_CREDENTIALS["password"]))
        self.second_user = UserFactory(username=self.SECOND_USER_CREDENTIALS["username"],
                                       email=self.SECOND_USER_CREDENTIALS["email"],
                                       password=generate_password_hash(self.VAlID_CREDENTIALS["password"]))
        self.third_user = UserFactory(username=self.THIRD_USER_CREDENTIALS["username"],
                                       email=self.THIRD_USER_CREDENTIALS["email"],
                                       password=generate_password_hash(self.THIRD_USER_CREDENTIALS["password"]))

    def _test_login(self, credentials, expect_success=True):
        resp = self.client.post(self.URL,
                                headers=self._HEADER_CONT_TYPE_JSON,
                                json=credentials)
        self._assert_successful_login(resp) if expect_success else self._assert_unsuccessful_login(resp)

    def _assert_successful_login(self, response):
        self.assert200(response)
        self.assertIn("token", response.json)
        token = response.json['token']
        decoded_token = AuthManager.decode_token(token)
        self.assertEqual(decoded_token['id'], self.user.id)

    def _assert_unsuccessful_login(self, response):
        self.assert400(response)
        self.assertEqual(response.json["message"], UserManager.CREDENTIALS_ERROR_MESSAGE)
    def test_login_via_email_valid_credentials_expect_200_and_return_token(self):
        credentials = {
            "identifier": self.VAlID_CREDENTIALS["email"],
            "password": self.VAlID_CREDENTIALS["password"]
        }
        self._test_login(credentials)

    def test_login_via_username_valid_credentials_expect_200_and_return_token(self):
        credentials = {
            "identifier": self.VAlID_CREDENTIALS["username"],
            "password": self.VAlID_CREDENTIALS["password"]
        }
        self._test_login(credentials)

    def test_login_invalid_password_expect_400_and_correct_json(self):
        credentials = {
            "identifier": self.VAlID_CREDENTIALS["username"],
            "password": "wrong password"
        }

        self._test_login(credentials, expect_success=False)

    def test_login_non_existing_identifier_expect_400_and_correct_json(self):
        credentials = {
            "identifier": "not_existing",
            "password": self.VAlID_CREDENTIALS["password"],
        }

        self._test_login(credentials, expect_success=False)

    def test_login_with_first_user_identifier_and_third_user_password_expect_400_and_correct_json(self):
        credentials = {
            "identifier": "not_existing",
            "password": self.VAlID_CREDENTIALS["password"],
        }

        self._test_login(credentials, expect_success=False)
