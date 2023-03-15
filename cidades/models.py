from django.db import models


class Location(models.Model):
    id = models.CharField(verbose_name="id", max_length=40, primary_key=True)
    verbose = models.CharField(verbose_name="verbose", max_length=255)

    name = models.CharField(verbose_name="name", max_length=255)
    state = models.CharField(verbose_name="state", max_length=255)

    def __str__(self):
        return self.verbose

