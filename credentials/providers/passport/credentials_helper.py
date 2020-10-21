from credentials.auth.jwt.rsa_signer import RSASigner
from .file_loader import load_passport_file


def get_credentials_helper(location):
    passport_data = load_passport_file(location)
    return RSASigner(passport_data['private_key'], passport_data['certificate_id'], passport_data['issuer'],
                     passport_data['subject_id'], 'RS256')
