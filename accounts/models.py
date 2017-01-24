from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_img = models.ImageField(blank=True)
    title = models.CharField(max_length=10)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'profile for %s' % self.user.username