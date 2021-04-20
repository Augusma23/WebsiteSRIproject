from django.db import models

class Article(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField(max_length=1000, default='SOME STRING')
    image_url=models.CharField(max_length=2000)