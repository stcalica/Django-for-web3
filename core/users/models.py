from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

class Web3UserManager(BaseUserManager):
    def create_user(self, public_address, **kwargs):
        user = self.model(public_address=public_address)
        user.save(using=self._db)
        return user

    def create_superuser(self, public_address, password, email=None):
        user = self.create_user(
        public_address=public_address,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Web3User(AbstractUser):
    username = None
    public_address = models.CharField(max_length=64, unique=True)
    nonce = models.CharField(max_length=64, default=uuid.uuid4().hex)
    is_creator = models.BooleanField(default=False)
    USERNAME_FIELD = "public_address"
    objects = Web3UserManager()

    #TODO: on_create to generate nonce
