from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    dish = models.CharField(max_length=255, default=" ")

    def __str__(self):
        return self.name
