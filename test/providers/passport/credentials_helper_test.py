from credentials.providers.passport.credentials_helper import get_passport_credentials_helper
import unittest
import pathlib
from os import path
from .fixture_helper import get_fixture_location


class TestGettingCredentialsHelper(unittest.TestCase):

    def test_getting_credentials_helper(self):
        helper = get_passport_credentials_helper(
            get_fixture_location('validPassport.json'))

        token = helper.get_token('test audience')

        number_of_segments = len(token.split('.'))

        self.assertEqual(number_of_segments, 3)


if __name__ == '__main__':
    unittest.main()
