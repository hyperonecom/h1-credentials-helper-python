from time import time
import jwt


class JWTSigner:
    def __init__(self, private_key, key_id, issuer, subject_id, algorithm):
        self.private_key = private_key
        self.key_id = key_id
        self.issuer = issuer
        self.subject_id = subject_id
        self.algorithm = algorithm

    def get_token(self, audience):
        current_unix_timestamp = int(time())
        five_minutes = 5 * 60
        payload = {
            "aud": audience,
            "iat": current_unix_timestamp,
            "exp": current_unix_timestamp + five_minutes,
            "sub": self.subject_id
        }
        headers = {'kid': self.key_id}

        token = jwt.encode(payload, self.private_key,
                           algorithm=self.algorithm, headers=headers)
        return token.decode('utf-8')
