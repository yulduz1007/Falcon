from django.db import models
from django.db.models import BooleanField


# Create your models here.
class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    information = BooleanField(default=False)

    def __str__(self):
        return self.title

