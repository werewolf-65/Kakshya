from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=150)
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    #voter=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
