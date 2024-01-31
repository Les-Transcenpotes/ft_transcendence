from django.test import TestCase
from django.test.client import os

from keys.publickey import public_key
from keys.privatekey import private_key

import jwt

# Create your tests here.

class testModelInsertion(TestCase):

    def testJWT(self):
        payload = {'exp': 'youpi'}

        encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
        print(encoded)
        decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
        print(decoded)

