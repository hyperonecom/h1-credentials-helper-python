from credentials.auth.jwt.jwt_signer import JWTSigner
from .file_loader import load_passport_file, get_default_passport_location


def get_passport_credentials_helper(location=get_default_passport_location()):
    passport_data = load_passport_file(location)
    return JWTSigner(passport_data['private_key'], passport_data['certificate_id'], passport_data['issuer'],
                     passport_data['subject_id'], 'RS256')
