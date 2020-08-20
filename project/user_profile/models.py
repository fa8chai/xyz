from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


CustomUser = settings.AUTH_USER_MODEL

class School(models.Model):
    name = models.CharField(unique=True,blank=False,max_length=80)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, related_name='students', null=True)
    passing_date = models.DateField(null=True)
    def __str__(self):
        if self.user.is_superuser:
            return f'Superuser ({self.user.name}) profile'
        return f'{self.user.name} Profile'
   
@receiver(post_save, sender=CustomUser)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
    instance.profile.save()

