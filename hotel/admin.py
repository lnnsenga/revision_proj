from django.contrib import admin
from .models import User, Customer, Staff, Room, Payment, Reservation, Booking, PaymentType, RoomStatus, RoomType

# Register your models here.
admin.site.register([User, Customer, Staff, Room, Payment, Reservation, Booking, PaymentType, RoomStatus, RoomType])
