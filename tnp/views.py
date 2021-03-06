from unicodedata import name
from django.shortcuts import render, redirect
from .models import Plane, Train, Car, Boat
from .forms import BoatForm, CarForm, TrainForm, PlaneForm


# Create your views here.

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'tnp/train_list.html', {'trains': trains})


def plane_list(request):
    planes = Plane.objects.all()
    return render(request, 'tnp/plane_list.html', {'planes': planes})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'tnp/car_list.html', {'cars': cars})


def boat_list(request):
    boats = Boat.objects.all()
    return render(request, 'tnp/boat_list.html', {'boats': boats})


def train_detail(request, pk):
    train = Train.objects.get(id=pk)
    return render(request, 'tnp/train_detail.html', {'train': train})


def plane_detail(request, pk):
    plane = Plane.objects.get(id=pk)
    return render(request, 'tnp/plane_detail.html', {'plane': plane})


def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'tnp/car_detail.html', {'car': car})


def boat_detail(request, pk):
    boat = Boat.objects.get(id=pk)
    return render(request, 'tnp/boat_detail.html', {'boat': boat})


def train_create(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            train = form.save()
            return redirect('train_detail', pk=train.pk)
    else:
        form = TrainForm()
    return render(request, 'tnp/train_form.html', {'form': form})


def plane_create(request):
    if request.method == 'POST':
        form = PlaneForm(request.POST)
        if form.is_valid():
            plane = form.save()
            return redirect('plane_detail', pk=plane.pk)
    else:
        form = PlaneForm()
    return render(request, 'tnp/plane_form.html', {'form': form})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'tnp/car_form.html', {'form': form})


def boat_create(request):
    if request.method == 'POST':
        form = BoatForm(request.POST)
        if form.is_valid():
            boat = form.save()
            return redirect('boat_detail', pk=boat.pk)
    else:
        form = BoatForm()
    return render(request, 'tnp/boat_form.html', {'form': form})


def train_edit(request, pk):
    train = Train.objects.get(pk=pk)
    if request.method == 'POST':
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            train = form.save()
            return redirect('train_detail', pk=train.pk)
    else:
        form = TrainForm(instance=train)
    return render(request, 'tnp/train_form.html', {'form': form})


def plane_edit(request, pk):
    plane = Plane.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlaneForm(request.POST, instance=plane)
        if form.is_valid():
            plane = form.save()
            return redirect('plane_detail', pk=plane.pk)
    else:
        form = PlaneForm(instance=plane)
    return render(request, 'tnp/plane_form.html', {'form': form})


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'tnp/car_form.html', {'form': form})


def boat_edit(request, pk):
    boat = Boat.objects.get(pk=pk)
    if request.method == 'POST':
        form = BoatForm(request.POST, instance=boat)
        if form.is_valid():
            boat = form.save()
            return redirect('boat_detail', pk=boat.pk)
    else:
        form = BoatForm(instance=boat)
    return render(request, 'tnp/boat_form.html', {'form': form})


def train_delete(request, pk):
    Train.objects.get(pk=pk).delete()
    return redirect('train_list')


def plane_delete(request, pk):
    Plane.objects.get(pk=pk).delete()
    return redirect('plane_list')


def car_delete(request, pk):
    Car.objects.get(pk=pk).delete()
    return redirect('car_list')


def boat_delete(request, pk):
    Boat.objects.get(pk=pk).delete()
    return redirect('boat_list')
