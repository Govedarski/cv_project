# from models import UserModel, CustomerModel
# from schemas.validators.common_validators import ValidateIsAlphaNumeric
# from schemas.validators.password_validator import PasswordValidator
# from tests.base_test_case import BaseTestCase
# from tests.constants import Endpoints
# from tests import helpers as test_helpers
#
#
# class TestUserRegistration(BaseTestCase):
#     URL = Endpoints.REGISTER_USER[0]
#     VALID_CUSTOMER_DATA = {
#         "username": "test",
#         "email": "test@test.com",
#         "password": "testP@ss1!"
#     }
#
#     def test_register_with_valid_data_expect_201_user_added_to_db_and_return_customer_token(self):
#         resp = self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=self.VALID_CUSTOMER_DATA)
#
#         self.assertEqual(201, resp.status_code)
#         self.assertIn("token", resp.json)
#         test_helpers.assert_count_equal(1, UserModel)
#         test_helpers.assert_count_equal(1, CustomerModel)
#
#     def test_register_existing_email_expect_400_customer_not_added_to_db(self):
#         self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=self.VALID_CUSTOMER_DATA)
#         test_helpers.assert_count_equal(1, CustomerModel)
#
#         resp = self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=self.VALID_CUSTOMER_DATA)
#
#         self.assert400(resp)
#         self.assertEqual("Email: test@test.com is already taken!", resp.json["message"])
#         test_helpers.assert_count_equal(1, CustomerModel)
#
#     def test_register_with_existing_username_expect_400_customer_not_added_to_db(self):
#         self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=self.VALID_CUSTOMER_DATA)
#         test_helpers.assert_count_equal(1, CustomerModel)
#
#         data = self.VALID_CUSTOMER_DATA | {"email": "test@example.com"}
#         resp = self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=data)
#
#         self.assert400(resp)
#         self.assertEqual("Username: test is already taken!", resp.json["message"])
#         test_helpers.assert_count_equal(1, CustomerModel)
#
#     def test_register_with_invalid_data_expect_400_customer_not_added_to_db_and_correct_json(self):
#         invalid_data = {
#             "username": "@a",
#             "email": "testtestcom",
#             "password": "s"
#         }
#
#         resp = self.client.post(self.URL, headers=self._HEADER_CONT_TYPE_JSON, json=invalid_data)
#
#         self.assert400(resp)
#         self.assertIn("Not a valid email address.", resp.json["message"]["email"])
#
#         [self.assertIn(message, resp.json["message"]["password"])
#          for message in PasswordValidator.policy_error_mapper.values()]
#
#         self.assertIn("Length must be between 3 and 64.", resp.json["message"]["username"])
#         self.assertIn(ValidateIsAlphaNumeric.ERROR, resp.json["message"]["username"])
#
#         test_helpers.assert_count_equal(0, CustomerModel)
