from django.contrib.auth.models import User
from django.db import models


# class Customer(AbstractUser):
#     # add additional fields in here
#     id_number = models.CharField(max_length=8)
#     phone_number = models.CharField(max_length=10)

#     def __str__(self):
#         return self.email

CATEGORY_CHOICES = [
    ('Standard Double Room', 'Standard Double Room'),
    ('Superior Double Room', 'Superior Double Room'),
    ('Family Room', 'Family Room'),
    ('Standard Single Room', 'Standard Single Room'),
    ('Superior Single Room', 'Superior Single Room'),
    ('VIP Room', 'VIP Room'),
]

class Category(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='hotel_pics')
    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField()
    number_of_beds = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    #TODO: Storing images

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.PositiveIntegerField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @property
    def available(self):
        pass

    def __str__(self):
        return "{} - {}".format(self.room_number, self.category.name)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
