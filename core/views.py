from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from core.backends import Web3Backend
import json

import logging
logger = logging.getLogger(__name__)

#TODO: user django rest framework to create nad serialize the users

@api_view(["POST"])
def get_token(request):
    public_address =  request.data["public_address"]
    web3 = Web3Backend()
    user, token = web3.authenticate(request)
    if token:
        return JsonResponse({'token': token})
    else:
        return HttpResponse('Authentication Failed')

def submit_nft_request(request):
    pass
