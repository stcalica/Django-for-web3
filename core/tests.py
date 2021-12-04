from rest_framework.test import APIClient
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView
from unittest import mock

from core.users.models import Web3UserManager
from core.users.models import Web3User
from core.auth.backends import Web3Backend


TEST_PUBLIC_ADDRESS = "0xsome_test_address"
TEST_NONEXISTENT_PUBLIC_ADDRESS = "0xnot_a_user"

import logging
logger = logging.getLogger(__name__)


class TestWeb3Manager(APITestCase):
    pass


class TestWeb3AuthBackend(APITestCase):
    def setUp(self):
        #TODO: set up test user
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_ExistingUser(self):
        self.user = Web3User(public_address=TEST_PUBLIC_ADDRESS)
        #TODO: create user with Web3Manager
        auth_backend = Web3Backend()
        #request = APIRequestFactory()
        post = self.factory.post('/api/token/', {'public_address': TEST_PUBLIC_ADDRESS, 'nonce': '0xsomething_random'},follow=True)
        request = APIView().initialize_request(post)
        with mock.patch.object(auth_backend, '_check_nonce', return_value=True) as method:
            try:
                token, user = auth_backend.authenticate(request)
                #TODO: assert user details are true
                #TODO: assert a token was created
                self.assertTrue(token)
                self.assertTrue(user)
            except Exception:
                logger.debug('Raised an exception')
                assert False

    def test_UserDoesNotExist(self):
        pass

    def test_NonceSignatureIsIncorrect(self):
        pass

    def test_GivenAnActiveToken(self):
        pass
