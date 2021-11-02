"""Dapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.auth.views import get_token
from core.auth.admin.views import login
from core.users.views import Web3UserList, Web3UserDetail, Web3UserCreate

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
#TODO: serperate api/user/<pk:string> as body and into POST vs GET
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', get_token, name='get_token'),
    path('api/users/', Web3UserList.as_view()),
    path('api/user/<str:public_address>', Web3UserDetail.as_view()),
    path('api/user/', Web3UserCreate.as_view()),
    path('/login', login, name='login'),
]
