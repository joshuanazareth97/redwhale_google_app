from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    display_picture = models.ImageField(
        upload_to = 'dps',
        help_text="Profile Picture",
        verbose_name="Profile Picture")

    @property
    def name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def update_user_profile(sender, obj, created, **kwargs):
    if created:
        Profile.objects.create(user=obj)
    obj.profile.save()
