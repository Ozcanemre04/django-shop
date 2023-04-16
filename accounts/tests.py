from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse,resolve
from rest_framework import status
from accounts.models import account
# Create your tests here.

class AccountRegisterTest(APITestCase):
     def test_create_account(self):
          url = reverse('rest_register')
          print(url)
          data = {
            "email": "foo@fo.com",
            "username": "emre",
            "password1": "foofoofoofoo",
            "password2": "foofoofoofoo",
            "first_name": "foo",
            "last_name": "bar",}
          response = self.client.post(url, data, format='json')
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(account.objects.count(), 1)
          self.assertEqual(account.objects.get().username, 'emre')



     def test_create_account_username_error(self):
          url = reverse('rest_register')
          print(url)
          data = {
            "email": "foo@fo.com",
            "username": "",
            "password1": "foofoofoofoo",
            "password2": "foofoofoofoo",
            "first_name": "foo",
            "last_name": "bar",}
          response = self.client.post(url, data, format='json')
          self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
          self.assertEqual(account.objects.count(), 0)
         

          