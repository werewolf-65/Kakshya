from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    members=models.ManyToManyField(User,related_name="members")
    doc=models.FileField(upload_to='projects/docs/')
    cover=models.ImageField(upload_to='projects/covers/',null=True,blank=True)
    stars=models.ManyToManyField(User,related_name="stars",blank=True)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def total_upvotes(self):
        return self.upvotes.count()
