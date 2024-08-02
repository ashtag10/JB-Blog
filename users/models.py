from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length= 100, blank=True, null=True)
    email= models.EmailField(unique= True)
    profile_picture= models.ImageField(upload_to="media/profiles/", null=True, blank=True, default="IMG_0254.jpg")
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = ["first_name","last_name", "username"]

# Create your models here.
