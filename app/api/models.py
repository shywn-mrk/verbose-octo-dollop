from statistics import mode
from django.db import models

class URL(models.Model):
    original_url = models.CharField(max_length=300)
    shorten_code = models.CharField(max_length=5)

    def __str__(self):
        return self.shorten_code
