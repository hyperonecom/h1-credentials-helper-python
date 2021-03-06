import json
from pathlib import Path
from os import path
from .exceptions import InvalidPassportException


def get_default_passport_location():
    return path.join(Path.home(), '.h1', 'passport.json')


def load_passport_file(location):
    with open(location, "r") as f:
        parsed_body = json.load(f)
        validate_passport(parsed_body)
        return parsed_body


def validate_passport(passport):
    if 'issuer' not in passport:
        raise InvalidPassportException("Issuer can't be empty")
    if 'certificate_id' not in passport:
        raise InvalidPassportException("Certificate_id can't be empty")
    if 'private_key' not in passport:
        raise InvalidPassportException("Private_key can't be empty")
    if 'subject_id' not in passport:
        raise InvalidPassportException("Subject_id can't be empty")
