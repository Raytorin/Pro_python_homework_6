import unittest
from main import list_city
from parameterized import parameterized


FIXTURE = [([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
], 'Россия')]


class TestListCity(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_list_city(self, geo_logs, etalon):
        result = list_city(geo_logs)
        for i in result:
            value = i.values()
            for value_inside in value:
                self.assertIn(etalon, value_inside)

