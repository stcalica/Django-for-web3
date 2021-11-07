from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

class Web3UserManager(BaseUserManager):
    def create_user(self, public_address, **kwargs):
        if not public_address:
            raise ValueError(_('The Public Address must be set'))
        user = self.model(public_address=public_address)
        user.set_unusable_password() #set unusable password for app users
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(
        public_address=username,
        username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Web3User(AbstractUser):
    public_address = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=40, unique=False, default='') #still exists in the abstract user model; needs to be non-unique and defaults to blank
    nonce = models.CharField(max_length=64, default=uuid.uuid4().hex)
    is_creator = models.BooleanField(default=False)
    USERNAME_FIELD = "public_address"
    objects = Web3UserManager()

    #TODO: on_create to generate nonce
    def __str__(self):
        return self.public_address
