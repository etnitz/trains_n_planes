from django.db import models

# Create your models here.
class Editor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    nationality = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    power_type = models.CharField(max_length=100)
    builder = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Plane(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Boat(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    builder = models.CharField(max_length=100)
    year = models.IntegerField()
    length = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name