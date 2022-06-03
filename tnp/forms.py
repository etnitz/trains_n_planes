from pyexpat import model
from django import forms
from .models import Train, Plane, Car, Boat

class TrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields= ('name', 'power_type', 'builder', 'year', 'country', 'description', 'photo_url')

class PlaneForm(forms.ModelForm):

    class Meta:
        model = Plane
        fields = ('name', 'role', 'manufacturer', 'year', 'country', 'description', 'photo_url')

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('name', 'type', 'manufacturer', 'year', 'country', 'description', 'photo_url')