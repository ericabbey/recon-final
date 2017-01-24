from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return '%s comment on %s with id %i' %(self.user.username, self.blog, self.blog_id)
