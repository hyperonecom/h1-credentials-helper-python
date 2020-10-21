from credentials.providers.passport.file_loader import load_passport_file
from credentials.providers.passport.exceptions import InvalidPassportException
import unittest


class TestLoadingCredentialsFile(unittest.TestCase):

    def test_loading_invalid_file(self):
        with self.assertRaises(InvalidPassportException):
            load_passport_file('./fixtures/invalidPassport.json')


if __name__ == '__main__':
    unittest.main()
