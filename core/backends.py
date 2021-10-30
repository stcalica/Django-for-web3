from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime
import jwt

#TODO: put into server environment
SECRET_KEY = "secret"

import logging
logger = logging.getLogger(__name__)

from core.models import Web3User

class Web3Backend(ModelBackend):
    '''
    1. Frontend will request a token through the /user?public_address={public_addressendpoint} sending a public address and expect a nonce the user model; Generated by us
        1a. no nonce then user does not exist
    2. User will sign their nonce with their private key and they will call /token with their signature/signed nonce and public_address
    3. We check the signature and nonce value; then generate a new nonce value and send back a JWT token
    4. We check the JWT token's expiry and if public_address is correct and it is unchanged to keep authenticating the user
        4a. if expiry or compromised we will not authenticate and ask user to go back to sign in flow in step 1
    https://www.toptal.com/ethereum/one-click-login-flows-a-metamask-tutorial
    https://uploads.toptal.io/blog/image/125792/toptal-blog-image-1522395353253-70fb1c40e9527154c2774507b63eac63.png
    '''
    def authenticate(self, request, **kwargs):
        public_address = request.data.get('public_address', None)
        nonce = request.data.get('nonce', None)
        curr_token = request.data.get('token', None)
        Web3User = get_user_model()

        if public_address:
            if curr_token:
                #TODO: decode token and check if public_address is the same as the user calling it and if not expired
                    #TODO: if yes then just return true and token
                return True, curr_token
                pass
            #TODO: decode the JWT and check if the user is the proper user
            try:
                #TODO: database check; will want to switch to JWT tokens in the future with refresh check to grab user
                web3user = Web3User.objects.get(public_address=public_address)
                #TODO: check nonce is signed correctly by user's private key by using the public key
                if ( web3user and self._check_nonce(nonce)):
                    logger.debug('everything passed')
                    logger.debug(web3user)
                    expiry = datetime.date.today() + datetime.timedelta(days=1)
                    token = jwt.encode({"user": public_address, "expiry": str(expiry) }, SECRET_KEY, algorithm="HS256")
                    return web3user, token
                else:
                    #TODO: return a 401 unauthorized
                    logger.debug('nonce not correct')
                    pass
            except Web3User.DoesNotExist:
                #TODO: return an exception response
                logger.debug('user not found')
                return Web3User.DoesNotExist
        else:
            #TODO: return a 204 to signify a user does not exist and have the frontend to send a POST /user request
            logger.debug('no nonce or public_address')
            return None, None


    def get_user(self, user_id):
        try:
            return Web3User.objects.get(pk=user_id)
        except Web3User.DoesNotExist:
            return None

    def _check_nonce(self, nonce):
        return True

#https://stackoverflow.com/questions/62739175/implement-djangorestframework-simplejwt-token-authentication-without-password
#https://dev.to/apcelent/json-web-token-based-authentication-backend-for-django-project-3n90
#MAYBE ONE DAY: maybe no JWT needed! https://medium.com/@bytesbay/you-dont-need-jwt-anymore-974aa6196976
