from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Calculus(models.Model):
    name = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = "calculus"