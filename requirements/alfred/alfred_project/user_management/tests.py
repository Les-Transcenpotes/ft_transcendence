from django.test import TestCase
from user_management.models import User

# Create your tests here.


class testAloneUserManagement(TestCase):
    def setUp(self):
        User.objects.create(
            unique_id=3,
            first_name="a",
            last_name="bah",
            pseudo="aba",
            email="abah@gmail.com")
        # user.save()
        User.objects.create(
            unique_id=2,
            first_name="a",
            last_name="bah",
            pseudo="abah",
            email="abah@gmail.com")
        # user.save()

    def test_getById(self):
        user = User.objects.create(
            unique_id=1,
            first_name="a",
            last_name="bah",
            pseudo="ghabah",
            email="abah@gmail.com")
        user.save()

        get = User.objects.get(unique_id=1)
        self.assertEqual(get, user)

    def test_newClient(self):

        pass


class testUserView(TestCase):
    def test_formIsComplete(self):
        pass
