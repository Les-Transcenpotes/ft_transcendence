from django.test import TestCase
from django.test.client import os

from keys.publickey import public_key
from keys.privatekey import private_key
from signin.models import Client

# Create your tests here.

class testModelInsertion(TestCase):
    def testCreateClient(self):
        test = Client(
                "a@oui.fr",
                "a",
                "pass",
                "ab",
                "last")


        self.assertTrue(1 == 2)


