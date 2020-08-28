from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email='jamali_arsalan_00@hotmail.com'
        password='Testpass'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):

        email= 'jamali_arsalan_00@HOTMAIL.COM'
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        email= 'jamali_arsalan_00@HOTMAIL.COM'
        user=get_user_model().objects.create_superuser(
            email,
            'pass100'
        )            

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)





