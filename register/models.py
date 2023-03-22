from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
  
    # name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, blank= True, null= True, default='P')
    visiblity = models.BooleanField(null=False, default=False)
    city = models.CharField(max_length=100, null= False, default='NA')
    state = models.CharField(max_length=100, null= False, default='NA')
    fullname = models.CharField(max_length=100, null= False, default='NA')
    profile_image = models.ImageField(upload_to='profile_images_dir/',default='default_profile_image.jpg')
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.city