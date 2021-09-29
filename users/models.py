from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import ugettext_lazy
from django.conf import settings



from .managers import CustomUserManager, CustomAdminManager



class MainUser(AbstractUser):
    username = None
    email = models.EmailField(ugettext_lazy('email adress'), unique=True)
    is_admin = models.BooleanField(default=False)
    is_simple_user = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # class Meta(AbstractUser.Meta):
    #      swappable = 'AUTH_USER_MODEL'


class CustomUser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    username = None
    email = models.EmailField(ugettext_lazy('email adress'), unique=True)


    is_admin = False
    is_simple_user = True


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # @property
    # def is_anonymous(self):
    #     return False

class CustomAdminUser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    username = None
    email = models.EmailField(ugettext_lazy('email adress'), unique=True)
    
    is_staff = True
    is_superuser = True

    is_admin = True
    is_simple_user = False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAdminManager()

    def __str__(self):
        return self.email

    # @property
    # def is_anonymous(self):
    #     return False