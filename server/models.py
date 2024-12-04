from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50, null=False)
    breed = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    weight = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    date = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"
