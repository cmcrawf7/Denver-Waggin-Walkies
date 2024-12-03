from django.contrib import admin
from .models import Dogs, User, Appointment

# Register your models here.
admin.site.register(Dogs)
admin.site.register(User)
admin.site.register(Appointment)
