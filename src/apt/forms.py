from django.forms import ModelForm,forms

from django.core.validators import MinValueValidator, MaxValueValidator
from .models import apartment

class apartmentForm(ModelForm):
    class Meta:
        model = apartment
        fields = ['name','city','address','rating','capacity','amenities']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) == 1:
            raise forms.ValidationError('Please enter a valid name')
        return name
