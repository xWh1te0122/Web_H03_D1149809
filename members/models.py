from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(default= 50)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # Create your models here.
    def __str__(self):
        return f"{self.firstname}{self.lastname}{self.age}"
    


    

