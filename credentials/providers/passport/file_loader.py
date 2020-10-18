import json


def load_passport_file(location):
    with open(location, "r") as f:
        body = f.read()
        parsed_body = json.loads(body)
        validate_passport(parsed_body)
        return parsed_body


def validate_passport(passport):
    errors = []
    keys = passport.keys()

    if not 'issuer' in keys:
        errors.append("Issuer can't be empty")
    if not 'certificate_id' in keys:
        errors.append("Certificate_id can't be empty")
    if not 'private_key' in keys:
        errors.append("Private_key can't be empty")
    if not 'subject_id' in keys:
        errors.append("Subject_id can't be empty")

    if len(errors) == 1:
        raise "Error when validating passport file: {}".format(errors[0])
    elif len(errors) > 1:
        raise "Multiple errors when validating passport file: {}".format(
            "\n".join(errors))
