from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password



class CustomUserManager(BaseUserManager):


    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_user(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True"
                )
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True"
                )
        return self._create_user(email, password, **extra_fields)


        # extra_fields.setdefault('is_superuser', True)
        # if extra_fields.setdefault('is_superuser') is not True:
        #     raise ValueError()
        # # return self.create_user(email, password, **extra_fields)        
        # if not email:
        #     raise ValueError(_('Email must be set'))
        # email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        # user.superuser = True
        # user.save()
        # return user



    # def create_super_user(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(_('Superuser must have is_superuser=True'))
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.is_superuser = True
    #     user.set_password(password)
    #     user.save()
    #     return user
        
        