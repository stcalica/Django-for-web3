from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.users.models import Web3User

admin.site.register(Web3User)
# class Web3UserInline(admin.StackedInline):
#     model = Web3User
#     can_delete = False
#     verbose_name_plural = 'web3users'
#
# class Web3UserAdmin(UserAdmin):
#     inlines = (Web3UserInline,)
#
# admin.site.register(Web3User, Web3UserAdmin)
