from django.db import models

class Email(models.Model):
    address = models.EmailField(unique=True)
    bmi=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.address
class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    age=models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()
    bmi=models.FloatField()

    def __str__(self):
        return self.name