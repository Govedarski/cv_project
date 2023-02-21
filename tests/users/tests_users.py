# import urllib.parse
# from unittest import TestCase
#
# from schemas.validators.common_validators import ValidateIsAlphaNumeric
# from tests.base_test_case import BaseTestCase
# from tests.constants import Endpoints
# from tests.factories import UserFactory, CustomerFactory, MerchantFactory, AdminFactory
# from tests.helpers import generate_token
#
#
# class TestGetUser(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         self.user = UserFactory()
#         self.url = Endpoints.GET_USER[0].replace("<int:pk>", str(self.user.id))
#
#     def test_get_with_existing_user_expect_200_and_correct_json(self):
#         resp = self.client.get(self.url)
#         self.assert200(resp)
#         self.assertEqual(self.user.id, resp.json["id"])
#         self.assertEqual(self.user.email, resp.json["email"])
#         self.assertEqual(self.user.username, resp.json["username"])
#
#
# class TestEditUser(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         self.user = UserFactory()
#         self.customer = CustomerFactory(id=self.user.id)
#         self.url = Endpoints.EDIT_USER[0].replace("<int:pk>", str(self.user.id))
#         token = generate_token(self.customer)
#         self._AUTHORIZATION_HEADER = {"Authorization": f"Bearer {token}"}
#         self._HEADERS = self._HEADER_CONT_TYPE_JSON | self._AUTHORIZATION_HEADER
#
#     def test_edit_valid_data_expect_200_change_save_in_db_and_correct_json(self):
#         data = {"username": "testUsername",
#                 "email": "test@example.com"}
#
#         resp = self.client.put(self.url, headers=self._HEADERS, json=data)
#         self.assert200(resp)
#         self.assertEqual(data["email"], resp.json["email"])
#         self.assertEqual(data["username"], resp.json["username"])
#         self.assertEqual(data["email"], self.user.email)
#         self.assertEqual(data["username"], self.user.username)
#
#     def test_edit_invalid_data_expect_400_and_correct_message(self):
#         data = {"username": "test_Username",
#                 "email": "testexamplecom"}
#
#         resp = self.client.put(self.url, headers=self._HEADERS, json=data)
#         self.assert400(resp)
#         self.assertIn(ValidateIsAlphaNumeric.ERROR, resp.json["message"]["username"])
#         self.assertIn("Not a valid email address.", resp.json["message"]["email"])
#
#     def test_edit_existing_email_expect_400_and_correct_message(self):
#         second_user = UserFactory()
#         data = {"username": second_user.username,
#                 "email": self.user.email}
#         resp = self.client.put(self.url, headers=self._HEADERS, json=data)
#         self.assert400(resp)
#         self.assertIn(f'Username: {second_user.username} is already taken!', resp.json["message"])
#
#     def test_edit_existing_username_expect_400_and_correct_message(self):
#         second_user = UserFactory()
#         data = {"username": self.user.username,
#                 "email": second_user.email}
#         resp = self.client.put(self.url, headers=self._HEADERS, json=data)
#         self.assert400(resp)
#         self.assertIn(f'Email: {second_user.email} is already taken!', resp.json["message"])
#
#
# class TestUserDeactivate(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         self.user = UserFactory()
#         self.customer = CustomerFactory(id=self.user.id)
#         self.merchant = MerchantFactory(id=self.user.id)
#         self.admin = AdminFactory(id=self.user.id)
#         self.url = Endpoints.DEACTIVATE_USER[0].replace("<int:pk>", str(self.user.id))
#         token = generate_token(self.customer)
#         self._AUTHORIZATION_HEADER = {"Authorization": f"Bearer {token}"}
#         self._HEADERS = self._HEADER_CONT_TYPE_JSON | self._AUTHORIZATION_HEADER
#
#     def test_deactivate_user_expect_204_and_deactivated_user(self):
#         resp = self.client.delete(self.url, headers=self._HEADERS)
#         self.assertEqual(204, resp.status_code)
#         self.assertFalse(self.customer.active)
#         self.assertFalse(self.merchant.active)
#         self.assertFalse(self.admin.active)
#         self.assertEqual("!", self.user.password[0])
#
#
# class TestGetUserList(BaseTestCase):
#     URL = Endpoints.GET_USER_LIST[0]
#
#     def test(self):
#         user = UserFactory(username="velko", email="super_gotin@gmail.com")
#         p=1
#         query_param = urllib.parse.quote(f'username=${self}')
#         url = self.URL + f'?where="{query_param}"&sort_by="username.desc'
#
#         self.client.get(url)
