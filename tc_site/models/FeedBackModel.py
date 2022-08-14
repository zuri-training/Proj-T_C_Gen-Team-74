from django.db import models
from django.contrib.auth.models import User

class FeedBackModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.user.username