from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.users.models import Web3User

admin.site.register(Web3User)
