import unittest
from python_repos import get_repo_data

class TestPythonRepos(unittest.TestCase):
    def test_api_call(self):
        status_code, get_call = get_repo_data()
        self.assertEqual(status_code, 200)

unittest.main()