from rest_framework.test import APIClient
from django.test import TestCase

from core.users.models import Web3UserManager

TEST_PUBLIC_ADDRESS = "0xsome_test_address"
TEST_NONEXISTENT_PUBLIC_ADDRESS = "0xnot_a_user"


class TestWeb3Manager(TestCase):
    pass


class TestWeb3AuthBackend(TestCase):
    pass
    # def test_authenticate(self):
    #     w3 = Web3UserManager()
    #     w3.create_user()
    #     authenticated_user = authenticate(public_address=user.email, password=user.password)
    #     self.assertEqual(authenticated_user, user)
