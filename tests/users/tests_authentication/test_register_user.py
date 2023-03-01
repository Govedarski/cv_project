from constants.endpoints import Endpoints
from models.user.user_model import UserModel
from schemas.validators.common_validators import ValidateIsAlphaNumericAndSpace
from schemas.validators.password_validator import PasswordValidator
from tests.base_test_case import BaseTestCase


class TestUserRegistration(BaseTestCase):
    URL = Endpoints.REGISTER_USER[0]
    VALID_USER_DATA = {
        "username": "test",
        "email": "test@test.com",
        "password": "testP@ss1!"
    }

    def test_register_with_valid_data_expect_201_user_added_to_db_and_return_token(self):
        resp = self.client.post(self.URL,
                                headers=self._HEADER_CONT_TYPE_JSON,
                                json=self.VALID_USER_DATA)

        self.assertEqual(201, resp.status_code)
        self.assertIn("token", resp.json)
        self._assert_count_equal(1, UserModel)
        token = resp.json['token']
        decoded_token = self._decode_token(token)
        self.assertEqual(1, decoded_token['id'])
        self.assertIn("user", resp.json)
        self.assertIn("id", resp.json["user"])
        self.assertIn("user_identifiers", resp.json["user"])
        self.assertEqual(resp.json["user"]["id"], resp.json["user"]["talent_id"])
        self.assertEqual(self.VALID_USER_DATA["email"], resp.json["user"]["email"])
        self.assertEqual(self.VALID_USER_DATA["username"], resp.json["user"]["username"])

    def test_register_existing_credential_expect_400_customer_not_added_to_db_and_correct_error(self):
        self.client.post(self.URL,
                         headers=self._HEADER_CONT_TYPE_JSON,
                         json=self.VALID_USER_DATA)

        self._assert_count_equal(1, UserModel)

        resp = self.client.post(self.URL,
                                headers=self._HEADER_CONT_TYPE_JSON,
                                json=self.VALID_USER_DATA)

        self.assert400(resp)
        self.assertEqual("is already taken!", resp.json["message"]["email"])
        self.assertEqual("is already taken!", resp.json["message"]["username"])
        self._assert_count_equal(1, UserModel)

    def test_register_with_invalid_data_expect_400_customer_not_added_to_db_and_correct_json(self):
        invalid_data = {
            "username": "@a",
            "email": "testtestcom",
            "password": "s"
        }

        resp = self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=invalid_data)

        self.assert400(resp)
        self.assertIn("Not a valid email address.", resp.json["message"]["email"])

        [self.assertIn(message, resp.json["message"]["password"])
         for message in PasswordValidator.policy_error_mapper.values()]

        self.assertIn("Length must be between 3 and 64.", resp.json["message"]["username"])
        self.assertIn("Must contain only letters and spaces!", resp.json["message"]["username"])
        self.assertIn(ValidateIsAlphaNumericAndSpace.ERROR, resp.json["message"]["username"])

        self._assert_count_equal(0, UserModel)
