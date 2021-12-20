from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import ugettext_lazy



class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(ugettext_lazy('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user