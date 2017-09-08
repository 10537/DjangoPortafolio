from django.db import models


# Create your models here.
class AdoptionPersonInfo(models.Model):
    name = models.CharField(help_text="Person's name", max_length=60)
    surname = models.CharField(help_text="Person's surname", max_length=60)
    birthday = models.DateField(help_text="Person's Birthday")
    age = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    sex = models.CharField(choices=(('male', 'Male'), ('female', 'Female')),
                           help_text="Person's sex", default='male', max_length=6)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class AdoptionRequest(models.Model):
    adopter = models.ForeignKey(AdoptionPersonInfo, null=True, blank=True)
    pets_number = models.IntegerField()
    reason = models.TextField()
