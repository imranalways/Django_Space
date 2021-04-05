from django.db import models

# Create your models here.
class Post(models.Model):
    PostId=models.CharField(max_length=150)
    UserId=models.CharField(max_length=150)
    PostBody=models.CharField(max_length=150)
    PostDate=models.DateTimeField(max_length=150)
    PostBy=models.CharField(max_length=150)
    PostUpdatedBy=models.CharField(max_length=150,null = True)
    PostUpdatedDate=models.DateTimeField(max_length=150,null = True)
    PostPrivacy=models.CharField(max_length=150)
    IsDeleted=models.CharField(max_length=150)