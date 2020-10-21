from credentials.providers.passport.file_loader import load_passport_file
from credentials.providers.passport.exceptions import InvalidPassportException
import unittest
import pathlib
from os import path
from .fixture_helper import get_fixture_location


class TestLoadingCredentialsFile(unittest.TestCase):

    def test_loading_invalid_file(self):
        with self.assertRaises(InvalidPassportException):
            load_passport_file(get_fixture_location('invalidPassport.json'))

    def test_loading_valid_file(self):
        loaded_passport = load_passport_file(
            get_fixture_location('validPassport.json'))

        self.assertEqual(
            loaded_passport["subject_id"], "/iam/project/projectId/sa/serviceAccountId")

        self.assertEqual(
            loaded_passport["certificate_id"], "certificateID"
        )

        self.assertEqual(
            loaded_passport["issuer"], "https://api.hyperone.com/v2/iam/project/projectId/sa/serviceAccountId"
        )

        # too long for assert equal testing
        self.assertNotEqual(loaded_passport["private_key"], "")


if __name__ == '__main__':
    unittest.main()
