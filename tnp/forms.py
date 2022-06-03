from django import forms
from .models import Train, Plane, Car, Boat

class TrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields= ('name', 'power_type', 'builder', 'year', 'country', 'description', 'photo_url')
        