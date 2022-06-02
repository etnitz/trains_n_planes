from django.shortcuts import render
from .models import Plane, Train, Car, Boat

# Create your views here.

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'tnp/train_list.html', {'trains':trains})

def plane_list(request):
    planes = Plane.objects.all()
    return render(request, 'tnp/plane_list.html', {'planes':planes})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'tnp/car_list.html', {'cars':cars})

def boat_list(request):
    boats = Boat.objects.all()
    return render(request, 'tnp/boat_list.html', {'boats':boats})

def train_detail(request, pk):
    train = Train.objects.get(id = pk)
    return render(request, 'tnp/train_detail.html', {'train':train})

