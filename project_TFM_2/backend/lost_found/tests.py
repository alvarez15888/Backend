from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import DjangoUser
from rest_framework.authtoken.models import Token

class FoundCreationTestCase(APITestCase):
    def setUp(self):
        self.found = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.found)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token' + self.token.key)

    def test_found_creation(self):
        dataf = {'obj':'Samnsung', 'serial':'1234WER456'}
        resf = self.client.post('/api_view/found/', dataf)
        self.assertEqual(resf.status_code, status.HTTP_201_CREATED)

    def test_found_creation_no_authorized(self):
        self.client.force_authenticate(found=None)
        dataf = {'obj':'Samnsung', 'serial':'1234WER456'}
        resf = self.client.post('/api_view/found/', dataf)
        self.assertEqual(resf.status_code, status.HTTP_403_FORBIDDEN)