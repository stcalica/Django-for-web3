from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# from jose import jws
# from django.http import HttpResponse
# import datetime
# from django.contrib.auth import authenticate


# def create_jwt(request):
#
#     """
#     the above token need to be saved in database, and a one-to-one
#     relation should exist with the username/user_pk
#     """
#
#     publicAddress = request.POST['username']
#     nonce = request.POST['password']
#     #user = authenticate(username=username, password=password)
#     expiry = datetime.date.today() + timedelta(days=1)
#     token = jws.sign({'username': user.username, 'expiry':expiry}, 'seKre8',  algorithm='HS256')

    return HttpResponse(token)

from core.models import Web3User

class Web3Backend(ModelBackend):
    #https://dev.to/apcelent/json-web-token-based-authentication-backend-for-django-project-3n90
    #TODO: create a view endpoint that returns a Django JWT token
    #TODO: use authenticate to check the JWT token rather than call the database

    #MAYBE ONE DAY: maybe no JWT needed! https://medium.com/@bytesbay/you-dont-need-jwt-anymore-974aa6196976

    def authenticate(self, request, **kwargs):
        Web3User = get_user_model()
        public_address = kwargs['public_address']
        nonce = kwargs['nonce']
        try:
            web3user = user.objects.get(public_address=public_address)
            # if web3user.user.check_password(password) is True:
            #     return customer.user
            #TODO: check nonce is signed correctly by user's private key by using the public key
            if (self._check_nonce(nonce)):
                return web3user
            else:
                #return a 401 unauthorized
                pass
        except Web3User.DoesNotExist:
            #return a 204 to signify a user does not exist and have the frontend to send a POST /user request
            pass

   def get_user(self, user_id):
        try:
            return Web3User.objects.get(pk=user_id)
        except Web3User.DoesNotExist:
            return None

    def _check_nonce(self, nonce):
        pass

    def _create_jwt(self, user):
        pass
        # address = user.publicAddress
        # expiry = datetime.date.today() + timedelta(days=1)
        #TODO: generate secret to be something more UUID like
        # token = jws.sign({'username': user.username, 'expiry':expiry}, 'secret',  algorithm='HS256')
        # return token
