from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.png',upload_to='profile_pics')
    birthdate=models.DateField(blank=True,null=True)
    bio=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,**kwargs):
        super().save() #run the save method of parent

        img = Image.open(self.image.path)

        if img.height >300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
