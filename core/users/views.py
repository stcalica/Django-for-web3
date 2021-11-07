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
        public_address = kwargs.get('public_address', None)
        if(public_address):
            try:
                user, created = Web3User.objects.get_or_create(public_address=public_address)
                if(created):
                    try:
                        serializer = Web3UserSerializer(user)
                        logger.debug(json.dumps(serializer.data))
                        return JsonResponse(serializer.data)
                    except Exception:
                        return Response({"message": "something went wrong with creating user"}, status=404)
                elif(user):
                    serializer = Web3UserSerializer(user)
                    return JsonResponse(serializer.data)
                else:
                    return Response({"message": "something went wrong with creating user"}, status=400)
            except Exception as e:
                return Response({"message": "user not found nor created", "exception": str(e)}, status=404)
            return JsonResponse(serializer.data)
        return Response({"message": "no public_address"}, status=400)
