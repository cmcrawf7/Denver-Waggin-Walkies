from django.contrib import admin
from .models import Dog, User, Appointment

# Register your models here.
admin.site.register(Dog)
admin.site.register(User)
admin.site.register(Appointment)
