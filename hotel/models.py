import uuid, random, string
from django.db import models


# Create your models here.

def generate_otp(length=6):
    """Generates a random numeric OTP of a specified length."""
    return ''.join(random.choices(string.digits, k=length))

def generate_payment_number():
    # Define the possible characters (uppercase letters and digits)
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random string of 7 characters
    random_part = ''.join(random.choices(characters, k=7))
    payment_number = "PM-"+random_part
    
    return payment_number


def generate_booking_number():
    # Define the possible characters (uppercase letters and digits)
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random string of 7 characters
    random_part = ''.join(random.choices(characters, k=7))
    booking_number = "BK-"+random_part
    
    return booking_number

def generate_reservation_number():
    # Define the possible characters (uppercase letters and digits)
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random string of 7 characters
    random_part = ''.join(random.choices(characters, k=7))
    reservation_number = "RS-"+random_part
    
    return reservation_number


class User(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address', max_length= 255, unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    otp_code = models.CharField(max_length=6,default=generate_otp,unique=True,editable=False, verbose_name="OTP Code")
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default =False)
    is_superadmin =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.username
  
class Customer(models.Model):
      
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),    
        ]
    
    STATUS_CHOICES = [
            ('Checked-in','Checked-in'),
            ('Checked-out','Checked-out'),  
            ('None','None'),     
        ]

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    user_id =models.OneToOneField(User,on_delete= models.SET_NULL, null=True, verbose_name="Username")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
    )

    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='None',
    )
    avatar_url =   avatar_url = models.URLField(
        max_length=300, 
        blank=True,      
        null=True   
        )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  
   


class Staff(models.Model):
      
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),    
        ]

    STAFF_TYPE=[
        ('Receptionist','Receptionist'),
        ('Manager','Manager'),
        ('Super Admin','Super Admin')
        ]
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    user_id =models.OneToOneField(User,on_delete= models.SET_NULL, null=True, verbose_name="Username")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',  
    )
    staff_type = models.CharField(
        max_length=13,
        choices=STAFF_TYPE,
        default='Receptionist',  
    )
    avatar_url =   avatar_url = models.URLField(
        max_length=300, 
        blank=True,      
        null=True   
        )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  

class RoomType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    type = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(
        max_digits=10,  
        decimal_places=2,  
    )
    description=models.TextField(max_length=200, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.type
  

class RoomStatus(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    status = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.status
  

 

class Room(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    room_type_id = models.ForeignKey(RoomType,on_delete=models.SET_NULL, null=True, verbose_name="Room Type")
    room_status_id = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True , verbose_name="Room Status")
    room_number = models.CharField( max_length= 3, null=True, verbose_name="Room Number")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
 
    def __str__(self):
        return f"{self.room_number} - {self.room_type_id} "
  



class PaymentType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
 
    def __str__(self):
        return self.name
  


class Payment(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    payment_number = models.CharField(max_length=15,default=generate_payment_number,unique=True,editable=False, verbose_name="Payment Number")
    payment_type_id = models.OneToOneField(PaymentType,on_delete=models.SET_NULL, null=True, blank=True, related_name='payment', verbose_name="Payment Mode")
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='payment', verbose_name="Customer Name")
    staff_id = models.ForeignKey(Staff, on_delete=models.RESTRICT, related_name='payment', verbose_name="Staff Name") 
    amount = models.DecimalField(
        max_digits=10,  
        decimal_places=2,  
    )
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.payment_number
  


class Booking(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    booking_number = models.CharField(max_length=15,default=generate_booking_number,unique=True,editable=False, verbose_name="Booking Number")
    room_id = models.OneToOneField(Room, on_delete=models.DO_NOTHING,null=True, blank=True,related_name='booking',verbose_name="Room Number")
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT,related_name='booking',verbose_name="Customer Name")
    staff_id = models.ForeignKey(Staff, on_delete=models.RESTRICT, related_name='booking',verbose_name="Staff Name")
    payment_id = models.OneToOneField(Payment, on_delete=models.RESTRICT, related_name='booking', verbose_name="Payment Number")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.booking_number
  



class Reservation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, auto_created=True)
    reservation_number = models.CharField(max_length=15,default=generate_reservation_number,unique=True,editable=False, verbose_name="Booking Number")
    room_id = models.OneToOneField(Room,on_delete=models.RESTRICT, related_name='reservation',  verbose_name="Room Number")
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='reservation', verbose_name="Customer Name")
    staff_id = models.ForeignKey(Staff, on_delete=models.RESTRICT, related_name='reservation', verbose_name="Staff Name")
    payment_id = models.ForeignKey(Payment, on_delete=models.RESTRICT, related_name='reservation', verbose_name="Payment Number")
    start_time = models.DateTimeField( null=True)
    end_time = models.DateTimeField( null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.reservation_number
  
