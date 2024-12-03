from django.db import models

# Create your models here.
class Dogs(models.Model):
    name = models.CharField(max_length=50, null=False)
    breed = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    weight = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name
    
class Appointment(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    date = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"
