from django import forms
from apps.adoptions.models import AdoptionPersonInfo, AdoptionRequest


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = AdoptionPersonInfo
        fields = [
            'name', 'surname', 'birthday', 'age', 'address', 'phone', 'email', 'sex',
        ]
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'birthday': 'Birthday',
            'age': 'Age',
            'address': 'Address',
            'phone': 'Phone',
            'email': 'Email',
            'sex': 'Sex',
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'surname': forms.TextInput(attrs={"class": "form-control"}),
            'birthday': forms.TextInput(attrs={"class": "form-control"}),
            'age': forms.TextInput(attrs={"class": "form-control"}),
            'address': forms.Textarea(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'sex': forms.Select(attrs={"class": "form-control"})
        }


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = [
            'pets_number', 'reason',
        ]
        labels = {
            'pets_number': 'Pets Number',
            'reason': 'Reason',
        }
        widgets = {
            'pets_number': forms.TextInput(attrs={"class": "form-control"}),
            'reason': forms.Textarea(attrs={"class": "form-control"}),
        }
