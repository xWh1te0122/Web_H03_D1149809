from django.db import models

class Court(models.Model):
    courtName = models.CharField(max_length=255)
    courtType = models.CharField(max_length=255)
    locationCity = models.CharField(max_length=255)
    address = models.CharField(max_length=255,null=True)
    # Create your models here.
    def __str__(self):
        return f"{self.courtName}{self.courtType}{self.locationCity}"