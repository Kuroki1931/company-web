from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=30, blank=False)
    keywords = JSONField()
    recruit = JSONField()
    news = JSONField()

    def __str__(self):
        return self.name