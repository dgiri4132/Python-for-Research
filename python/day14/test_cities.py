import unittest
from day14exercises import city_country


class NameTestClass(unittest.TestCase):
    def test_city_country(self):
        country_city=city_country('santiago','chile')
        self.assertEqual(country_city,'santiago, chile')

unittest.main()