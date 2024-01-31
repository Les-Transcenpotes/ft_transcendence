from django.test import TestCase
# from signin.models import Client
from myjwt.refresher import JWT

class testClient(TestCase):
    def test_to_dict(self):
        pass

class testJWT(TestCase):
    def testJWT(self):
        dict = {"bonjour": "toi"}
        marquer,  content = JWT.payloadToJwt(dict)
        if not marquer:
            print(content)
            return
        encoded = content
        marquer, content = JWT.jwtToPayload(encoded)
