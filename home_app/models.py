from django.db import models

class Footer(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()