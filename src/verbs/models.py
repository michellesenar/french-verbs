from django.db import models


class FrenchVerb(models.Model):
    english = models.CharField(max_length=40)
    french = models.CharField(max_length=40)
    french_ascii = models.CharField(max_length=40)
