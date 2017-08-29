from django.db import models
from apps.adoptions.models import AdoptionPersonInfo
from apps.medical.models import MedicalInfo


# Create your models here.
class Pets(models.Model):
    name = models.CharField(help_text="Your Pet's name", max_length=60)
    sex = models.CharField(choices=(('male', 'Male'), ('female', 'Female')),
                           help_text="Your Pet's sex", default='male', max_length=6)
    birthday = models.DateField(help_text="Your Pet's birthday")
    age = models.FloatField(help_text="Your Pet's ages")
    owner = models.ForeignKey(AdoptionPersonInfo, null=True, blank=True, on_delete=models.CASCADE)
    medical_info = models.OneToOneField(MedicalInfo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
