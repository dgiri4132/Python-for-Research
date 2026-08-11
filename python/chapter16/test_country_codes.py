import unittest
from country_codes import get_country_code

class NamesTestCase(unittest.TestCase):
    def test_get_code(self):
        get_code = get_country_code('Bolivia')
        self.assertEqual(get_code, 'bo')

unittest.main()