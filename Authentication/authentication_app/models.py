from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


# Creating the MyUserManager 

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email")

        email=self.normalize_email(email)
        user=self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_active=True
        user.save(using=self._db)
        return user


        # normalize_email(email) changes the value to lower case


class MyUser(AbstractBaseUser):
    identifier=models.CharField(max_length=40, unique=True)
    email=models.EmailField(max_length=255, unique=True)
    joined_date=models.DateTimeField(default=datetime.datetime.now(),blank=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD ='email'

    def __unicode__(self):
        return self.email

    def get_user(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    objects=UserProfileManager()

# As Django suggests:
# has_perm() returns True if the user has the specified permission.If the user is
# inactive, this method will always return False.
# has_module_perms() returns True if the user has any permissions in the given 
# package.






