from django.db import models

# Create your models here.
class React(models.Model):
    prompt = models.CharField(max_length=300)
