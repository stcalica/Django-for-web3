from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from core.auth.backends import Web3Backend
import json

import logging
logger = logging.getLogger(__name__)

#TODO: user django rest framework to create nad serialize the users

#expects public_address, nonce and token if user is currently signed in
@api_view(["POST"])
def login(request):
    token =  request.data["token"]
    web3 = Web3Backend()
    user, token = web3.authenticate(request)
    if(user and token):
        return True