from django.db import models


class FrenchVerb(models.Model):
    id = models.AutoField(primary_key=True)
    english = models.CharField(max_length=40)
    french = models.CharField(max_length=40)
    french_ascii = models.CharField(max_length=40)
