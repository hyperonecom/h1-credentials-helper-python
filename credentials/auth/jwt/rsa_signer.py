import jwt


class RSASigner:
    def __init__(self, private_key, key_id, issuer, subject_id, algorithm):
        self.private_key = private_key
        self.key_id = key_id
        self.issuer = issuer
        self.subject_id = subject_id
        self.algorithm = algorithm

    def get_token(self, audience):
        return jwt.encode({}, self.private_key, algorithm=self.algorithm)
