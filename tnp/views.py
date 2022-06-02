from django.shortcuts import render
from .models import Plane, Train, Car, Boat

# Create your views here.

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'tnp/train_list.html', {'trains':trains})

def plane_list(request):
    planes = Plane.objects.all()
    return render(request, 'tnp/plane_list.html', {'planes':planes})

