import unittest
import json
from time import time
from base64 import b64decode
from credentials.auth.jwt.jwt_signer import JWTSigner

PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgGFfgMY+DuO8l0RYrMLhcl6U/NigNIiOVhoo/xnYyoQALpWxBaBR
+iVJiBUYunQjKA33yAiY0AasCfSn1JB6asayQvGGn73xztLjkeCVLT+9e4nJ0A/o
dK8SOKBg9FFe70KJrWjJd626el0aVDJjtCE+QxJExA0UZbQp+XIyveQXAgMBAAEC
gYBHcL1XNWLRPaWx9GlUVfoGYMMd4HSKl/ueF+QKP59dt5B2LTnWhS7FOqzH5auu
17hkfx3ZCNzfeEuZn6T6F4bMtsQ6A5iT/DeRlG8tOPiCVZ/L0j6IFM78iIUT8XyA
miwnSy1xGSBA67yUmsLxFg2DtGCjamAkY0C5pccadaB7oQJBAKsIPpMXMni+Oo1I
kVxRyoIZgDxsMJiihG2YLVqo8rPtdErl+Lyg3ziVyg9KR6lFMaTBkYBTLoCPof3E
AB/jyucCQQCRv1cVnYNx+bfnXsBlcsCFDV2HkEuLTpxj7hauD4P3GcyLidSsUkn1
PiPunZqKpsQaIoxc/BzTOCcP19ifgqdRAkBJ8Cp9FE4xfKt7YJ/WtVVCoRubA3qO
wdNWPa99vgQOXN0lc/3wLevSXo8XxRjtyIgJndT1EQDNe0qglhcnsiaJAkBziAcR
/VAq0tZys2szf6kYTyXqxfj8Lo5NsHeN9oKXJ346xkEtb/VsT5vQFGJishsU1HoL
Y1W+IO7l4iW3G6xhAkACNwtqxSRRbVsNCUMENpKmYhsyN8QXJ8V+o2A9s+pl21Kz
HIIm179mUYCgO6iAHmkqxlFHFwprUBKdPrmP8qF9
-----END RSA PRIVATE KEY-----'''


class TestJwtRsaSigner(unittest.TestCase):

    def test_getting_token(self):
        signer = JWTSigner(PRIVATE_KEY, 'key_id',
                           'issuer', 'subject_id', 'RS256')

        token = signer.get_token('audience')
        segments = token.split('.')

        self.assertEqual(len(segments), 3)

        header = decode_jwt_segment(segments[0])
        self.assertEqual(header['kid'], 'key_id')
        self.assertEqual(header['alg'], 'RS256')

        payload = decode_jwt_segment(segments[1])
        self.assertEqual(payload['aud'], 'audience')
        self.assertEqual(payload['iss'], 'issuer')
        self.assertEqual(payload['sub'], 'subject_id')
        current_unix_timestamp = int(time())
        self.assertGreaterEqual(payload['iat'], current_unix_timestamp)
        self.assertGreaterEqual(payload['exp'], current_unix_timestamp)
        self.assertGreaterEqual(payload['exp'], payload['iat'])


def decode_jwt_segment(segment):
    decoded_message = decode_base64(segment)
    return json.loads(decoded_message)


def decode_base64(b64_string):
    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += '=' * (4 - missing_padding)
    encoded_bytes = b64_string.encode('ascii')
    decoded_bytes = b64decode(encoded_bytes)
    return decoded_bytes.decode('ascii')


if __name__ == '__main__':
    unittest.main()
