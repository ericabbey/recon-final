from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    content = models.TextField()

    def __str__(self):
        return self.name