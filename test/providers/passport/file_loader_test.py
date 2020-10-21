from credentials.providers.passport.file_loader import load_passport_file, get_default_passport_location
from credentials.providers.passport.exceptions import InvalidPassportException
import unittest
from unittest.mock import patch
import pathlib
from os import path
from .fixture_helper import get_fixture_location
from pathlib import WindowsPath, Path


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


class TestPassportValidation(unittest.TestCase):
    pass


class TestGettingDefaultPassportLocation(unittest.TestCase):

    def test_getting_passport_location(self):
        with patch.object(Path, 'home') as mock:
            path_object_mock = WindowsPath("C:/Users/Jakup")
            mock.return_value = path_object_mock

            passport_path = get_default_passport_location()
            self.assertEqual(
                passport_path, "C:\\Users\\Jakup\\.h1\\passport.json")


if __name__ == '__main__':
    unittest.main()
