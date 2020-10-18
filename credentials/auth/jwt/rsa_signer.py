import jwt


class RSASigner():
    def __init__(self, private_key, key_id, issuer, subject_id, algorithm='RS256'):
        self.private_key = private_key
        self.key_id = key_id
        self.issuer = issuer
        self.subject_id = subject_id
        self.algorithm = algorithm

    def getToken(self, audience):
        return jwt.encode({}, self.private_key, self.algorithm)
