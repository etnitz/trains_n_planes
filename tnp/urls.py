from django.urls import path
from . import views

urlpatterns = [
    path('trains/', views.train_list, name='train_list'),
    path('planes/', views.plane_list, name='plane_list'),
    path('cars/', views.car_list, name='car_list'),
    path('boats/', views.boat_list, name='boat_list'),
    path('trains/<int:pk>', views.train_detail, name='train_detail')
]