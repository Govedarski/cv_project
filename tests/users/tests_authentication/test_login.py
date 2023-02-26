from werkzeug.security import generate_password_hash

from constants.endpoints import Endpoints
from constants.strings import IDENTIFIER, PASSWORD, USERNAME, EMAIL
from managers.user_manager import UserManager
from tests.base_test_case import BaseTestCase
from tests.factories.user_factory import UserFactory


class TestLoginCustomer(BaseTestCase):
    URL = Endpoints.LOGIN_USER[0]
    VAlID_CREDENTIALS = {
        USERNAME: "test",
        EMAIL: "test@test.com",
        PASSWORD: "testP@ss1!",
    }
    SECOND_USER_CREDENTIALS = {
        USERNAME: "second test",
        EMAIL: "secondtest@test.com",
    }
    THIRD_USER_CREDENTIALS = {
        USERNAME: "third test",
        EMAIL: "thirdtest@test.com",
        PASSWORD: "testP@ss2!",
    }

    def setUp(self):
        super().setUp()
        self.user = UserFactory(username=self.VAlID_CREDENTIALS[USERNAME],
                                email=self.VAlID_CREDENTIALS[EMAIL],
                                password=generate_password_hash(self.VAlID_CREDENTIALS[PASSWORD]))
        self.second_user = UserFactory(username=self.SECOND_USER_CREDENTIALS[USERNAME],
                                       email=self.SECOND_USER_CREDENTIALS[EMAIL],
                                       password=generate_password_hash(self.VAlID_CREDENTIALS[PASSWORD]))
        self.third_user = UserFactory(username=self.THIRD_USER_CREDENTIALS[USERNAME],
                                       email=self.THIRD_USER_CREDENTIALS[EMAIL],
                                       password=generate_password_hash(self.THIRD_USER_CREDENTIALS[PASSWORD]))

    def _test_login(self, credentials, expect_success=True):
        resp = self.client.post(self.URL,
                                headers=self._HEADER_CONT_TYPE_JSON,
                                json=credentials)
        self._assert_successful_login(resp) if expect_success else self._assert_unsuccessful_login(resp)

    def _assert_successful_login(self, response):
        self.assert200(response)
        self.assertIn("token", response.json)
        token = response.json['token']
        decoded_token = self._decode_token(token)
        self.assertEqual(self.user.id, decoded_token['id'])

    def _assert_unsuccessful_login(self, response):
        self.assert400(response)
        self.assertEqual(UserManager.CREDENTIALS_ERROR_MESSAGE, response.json["message"])
    def test_login_via_email_valid_credentials_expect_200_and_return_token(self):
        credentials = {
            IDENTIFIER: self.VAlID_CREDENTIALS[EMAIL],
            PASSWORD: self.VAlID_CREDENTIALS[PASSWORD]
        }
        self._test_login(credentials)

    def test_login_via_username_valid_credentials_expect_200_and_return_token(self):
        credentials = {
            IDENTIFIER: self.VAlID_CREDENTIALS[USERNAME],
            PASSWORD: self.VAlID_CREDENTIALS[PASSWORD]
        }
        self._test_login(credentials)

    def test_login_invalid_password_expect_400_and_correct_json(self):
        credentials = {
            IDENTIFIER: self.VAlID_CREDENTIALS[USERNAME],
            PASSWORD: "wrong password"
        }

        self._test_login(credentials, expect_success=False)

    def test_login_non_existing_identifier_expect_400_and_correct_json(self):
        credentials = {
            IDENTIFIER: "not_existing",
            PASSWORD: self.VAlID_CREDENTIALS[PASSWORD],
        }

        self._test_login(credentials, expect_success=False)

    def test_login_with_first_user_identifier_and_third_user_password_expect_400_and_correct_json(self):
        credentials = {
            IDENTIFIER: "not_existing",
            PASSWORD: self.VAlID_CREDENTIALS[PASSWORD],
        }

        self._test_login(credentials, expect_success=False)
