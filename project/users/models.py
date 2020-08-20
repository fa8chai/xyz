from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User 
from phonenumber_field.modelfields import PhoneNumberField
from user_profile.models import Profile



class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(phone = phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, phone, password, **extra_fields):
        
        user = self.create_user(phone, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(('name'), max_length=60, blank=False)
    email = models.EmailField(('email address'))
    phone = PhoneNumberField(unique=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    is_superuser = models.BooleanField('superuser', default=False)
    is_staff = models.BooleanField('staff', default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
        
    def get_email(self):
        return self.email
        
    def get_phone(self):
        return self.phone

