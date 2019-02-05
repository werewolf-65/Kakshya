from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    upvotes=models.ManyToManyField(User,related_name="upvotes",blank=True)
    img=models.FileField(upload_to='gallery/',null=True,blank=True) #soon to be an image upload feature
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_posted',]
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')
    #    return reverse('post-detail',kwargs={'pk':self.pk})
        #returns the full path as a string

    def total_upvotes(self):
        return self.upvotes.count()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.post.title,self.user.username)
