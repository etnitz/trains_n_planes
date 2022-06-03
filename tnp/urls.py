from django.urls import path
from . import views

urlpatterns = [
    path('trains/', views.train_list, name='train_list'),
    path('planes/', views.plane_list, name='plane_list'),
    path('cars/', views.car_list, name='car_list'),
    path('boats/', views.boat_list, name='boat_list'),
    path('trains/<int:pk>', views.train_detail, name='train_detail'),
    path('planes/<int:pk>', views.plane_detail, name='plane_detail'),
    path('cars/<int:pk>', views.car_detail, name='car_detail'),
    path('boats/<int:pk>', views.boat_detail, name='boat_detail'),
    path('trains/new', views.train_create, name='train_create'),
    path('planes/new', views.plane_create, name='plane_create'),
    path('cars/new', views.car_create, name='car_create'),
    path('boats/new', views.boat_create, name='boat_create'),
    path('trains/<int:pk>/edit', views.train_edit, name='train_edit'),
    path('planes/<int:pk>/edit', views.plane_edit, name='plane_edit'),
    path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('boats/<int:pk>/edit', views.boat_edit, name='boat_edit')
]