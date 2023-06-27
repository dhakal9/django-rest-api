from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=3000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
