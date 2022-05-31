from django.contrib import admin
from .models import Editor, Train, Plane, Car

# Register your models here.

admin.site.register(Editor)
admin.site.register(Train)
admin.site.register(Plane)
admin.site.register(Car)