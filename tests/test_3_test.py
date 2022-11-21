import unittest
from test_3 import max_sales
from parameterized import parameterized


FIXTURE = [({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex')]


class TestListCity(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_list_city(self, stats, etalon):
        result = max_sales(stats)
        self.assertEqual(result, etalon)
