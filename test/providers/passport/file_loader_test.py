from ....credentials.providers.passport.file_loader import load_passport_file
import unittest


class TestLoadingCredentialsFile(unittest.TestCase):

    def test_loading_invalid_file(self):
        self.assertRaises(Exception, load_passport_file(
            './fixtures/invalidPassport.json'))


if __name__ == '__main__':
    unittest.main()
