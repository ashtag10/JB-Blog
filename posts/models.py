from django.db import models
from users.models import BlogUser

class Post(models.Model):
    title= models.CharField(max_length=100, blank=True, null=True)
    body= models.TextField()
    author= models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated= models.DateTimeField(auto_now=True, blank=True, null=True)

 
   
class Comment(models.Model):
    comment= models.TextField(blank=True, null=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)

# Create your models here.
