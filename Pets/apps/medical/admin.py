from django.contrib import admin
from apps.medical.models import Vaccines, MedicalInfo

# Register your models here.
admin.site.register(Vaccines)
admin.site.register(MedicalInfo)
