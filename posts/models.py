from __future__ import unicode_literals
from vote.managers import VotableManager

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120, blank=True)

    image = models.ImageField(null=True, blank=True, height_field="height", width_field="width")
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    num_votes = models.PositiveIntegerField(default=0)
    votes = VotableManager(extra_field='num_vote')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp"]
