from django.test import TestCase
from alfred_project.user_management.models import User

class userManagementTest(TestCase):


    def testCreateUser(self):
        to_create = User()
        to_create.email = b"bonjour@gmail.com"


