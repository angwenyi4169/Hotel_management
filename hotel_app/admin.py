from django.contrib import admin
from .models import (Room, Category, Booking)

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Category)
