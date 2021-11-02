from rest_framework import serializers
from core.users.models import Web3User

class Web3UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web3User
        fields = ['id', 'public_address', 'nonce', 'is_creator']
        read_only_fields = ['id', 'public_address', 'nonce', 'is_creator']
