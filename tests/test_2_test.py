import unittest
from test_2 import unique_numbers


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

etalon = [213, 15, 54, 119, 98, 35]


class TestListCity(unittest.TestCase):
    def test_list_city(self):
        etalon.sort()
        result = unique_numbers(ids)
        self.assertEqual(result, etalon)
