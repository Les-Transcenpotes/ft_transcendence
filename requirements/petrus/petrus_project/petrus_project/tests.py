from django.test import TestCase
# from signin.models import Client
from myjwt.jwt import JWT

class testClient(TestCase):
    def test_to_dict(self):
        pass

class testJWT(TestCase):
    def testJWT(self):
        dict = {"bonjour": "toi"}
        marquer,  content = JWT.payloadToJwt(dict, JWT.privateKey)
        if not marquer:
            return
        encoded = content
        if marquer:
            marquer, content = JWT.jwtToPayload(encoded, JWT.publicKey)
        self.assertEqual(content, dict)

    def testdate(self):
        print(JWT.peremptionDict())
