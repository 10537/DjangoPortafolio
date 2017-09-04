from django import forms
from apps.pets.models import Pets


class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = [
            'name', 'sex', 'birthday', 'age', 'owner', 'medical_info',
        ]
        labels = {
            'name': 'Name',
            'sex': 'Sex',
            'birthday': 'Birthday',
            'age': 'Age',
            'owner': 'Owner',
            'medical_info': 'Medical Info',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'medical_info': forms.Select(attrs={'class':'form-control'}),
        }