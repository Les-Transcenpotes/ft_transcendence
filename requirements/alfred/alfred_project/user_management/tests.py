from django.test import TestCase
from user_management.models import User

# Create your tests here.

class testAloneUserManagement(TestCase):
    def test1(self):
        user = User.objects.create(
                unique_id=1,
                first_name="a",
                last_name="bah",
                pseudo="abah",
                email="abah@gmail.com")
        user.save()

        get = User.objects.get(unique_id=1)
        self.assertEqual(get, user)

    def test2(self):
        pass

