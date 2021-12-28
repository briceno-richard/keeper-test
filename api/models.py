from django.db import models

class WebBookmark(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
