from django import forms
from .models import EnvironmentalData


class EnvironmentalForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalData
        fields = [
            'temperature',
            'rainfall',
            'humidity',
            'nitrogen',
            'phosphorus',
            'potassium'
        ]