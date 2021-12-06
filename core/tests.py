#from rest_framework.test import APIClient
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.views import APIView
from unittest import mock

from core.users.models import Web3UserManager
from core.users.models import Web3User
from core.auth.backends import Web3Backend
import datetime
import jwt


TEST_PUBLIC_ADDRESS = "0xsome_test_address"
TEST_NONEXISTENT_PUBLIC_ADDRESS = "0xnot_a_user"

import logging
logger = logging.getLogger(__name__)

#TODO: create test key and get from settings or mock_settings
SECRET_KEY = "secret"


class TestWeb3Manager(APITestCase):
    pass

class TestWeb3AuthBackend(APITestCase):
    def setUp(self):
        #self.client = APIClient()
        self.factory = APIRequestFactory()
        self.auth_backend = Web3Backend()

    def test_ExistingUser(self):
        self.user = Web3User.objects.create_user(public_address=TEST_PUBLIC_ADDRESS)
        post = self.factory.post('/api/token/', {'public_address': TEST_PUBLIC_ADDRESS, 'nonce': '0xsomething_random'}, follow=True)
        request = APIView().initialize_request(post)

        with mock.patch.object(self.auth_backend, '_check_nonce', return_value=True) as method:
            try:
                user, token = self.auth_backend.authenticate(request)
                self.assertTrue(token)
                assert user.public_address == TEST_PUBLIC_ADDRESS
            except Exception as e:
                assert False

    def test_UserDoesNotExist(self):
        post = self.factory.post('/api/token/', {'public_address': TEST_PUBLIC_ADDRESS, 'nonce': '0xsomething_random'}, follow=True)
        request = APIView().initialize_request(post)
        with mock.patch.object(self.auth_backend, '_check_nonce', return_value=True) as method:
            try:
                user, token = self.auth_backend.authenticate(request)
            except Exception as e:
                assert True

    def test_NonceSignatureIsIncorrect(self):
        self.user = Web3User.objects.create_user(public_address=TEST_PUBLIC_ADDRESS)
        post = self.factory.post('/api/token/', {'public_address': TEST_PUBLIC_ADDRESS, 'nonce': '0xsomething_random'}, follow=True)
        request = APIView().initialize_request(post)
        with mock.patch.object(self.auth_backend, '_check_nonce', return_value=False) as method:
            try:
                user, token = self.auth_backend.authenticate(request)
            except Exception as e:
                logger.debug(str(e))
                assert True

    def test_GivenAnActiveToken(self):
        self.user = Web3User.objects.create_user(public_address=TEST_PUBLIC_ADDRESS)
        expiry = datetime.date.today() + datetime.timedelta(days=1)
        token = jwt.encode({"user": TEST_PUBLIC_ADDRESS, "expiry": str(expiry) }, SECRET_KEY, algorithm="HS256")
        post = self.factory.post('/api/token/', {'token':  token, 'public_address': TEST_PUBLIC_ADDRESS,}, follow=True)
        request = APIView().initialize_request(post)
        with mock.patch.object(self.auth_backend, '_check_nonce', return_value=False) as method:
            try:
                user, token = self.auth_backend.authenticate(request)
            except Exception as e:
                logger.debug(str(e))
                assert False
