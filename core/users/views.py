from core.users.models import Web3User
from core.users.serializers import Web3UserSerializer
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpResponse

import rest_framework.permissions as permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

import uuid, json

import logging
logger = logging.getLogger(__name__)

class Web3UserList(generics.ListCreateAPIView):
    queryset = Web3User.objects.all()
    serializer_class = Web3UserSerializer


class Web3UserDetail(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, **kwargs):
        logger.debug('attempting to get user')
        logger.debug(request.data)
        public_address = kwargs.get('public_address', None)
        logger.debug(public_address)
        if(public_address):
            try:
                web3user = Web3User.objects.get(public_address=public_address)
                serializer = Web3UserSerializer(web3user)
            except Exception:
                return Http404('User does not exist')
            return JsonResponse(serializer.data)
        return HttpResponseBadRequest('missing public address')

class Web3UserCreate(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        public_address = request.data.get('public_address', None)
        if(public_address):
            try:
                #TODO: missing nonce in serializer?
                created = Web3User.objects.get_or_create(public_address=public_address, nonce=uuid.uuid4().hex)
                if(created):
                    try:
                        web3user = Web3User.objects.get(public_address=public_address)
                        serializer = Web3UserSerializer(web3user)
                        logger.debug('user was created')
                        logger.debug(json.dumps(serializer.data))
                        return JsonResponse(serializer.data)
                    except Exception:
                        return Http404('Something went wrong with creating user')
                else:
                    return HttpResponseBadRequest('something went wrong with creating')
            except Exception:
                return Http400('User was not created')

        else:
            return HttpResponseBadRequest('missing public address')
