import unittest
import os
from yandex_auth import auth_page
from parameterized import parameterized


login = ''
password = ''
abspath_to_driver = os.path.abspath("firefoxdriver/geckodriver")

FIXTURE = [(login, password, abspath_to_driver, '200')]


class TestAuthPage(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_list_city(self, user_login, user_password, abspath, etalon):
        result = auth_page(user_login, user_password, abspath)
        self.assertEqual(result, etalon)
