from django.contrib import admin
from .models import Patient, Plan, Line

# Register your models here.
admin.site.register(Patient)
admin.site.register(Plan)
admin.site.register(Line)

