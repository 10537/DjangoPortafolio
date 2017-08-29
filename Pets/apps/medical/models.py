from django.db import models


# Create your models here.
class Vaccines(models.Model):
    name = models.CharField(max_length=60, help_text="vaccine's name")

    def __str__(self):
        return self.name


class MedicalInfo(models.Model):
    doctor = models.CharField(max_length=60, help_text="Doctor's name")
    observations = models.TextField()
    weight = models.FloatField()
    height = models.FloatField()
    vaccines = models.ManyToManyField(Vaccines, blank=True)

    def __str__(self):
        return self.doctor
