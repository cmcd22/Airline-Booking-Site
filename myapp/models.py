from django.db import models

class Customer(models.Model):
    email = models.CharField(max_length=50,primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.IntegerField()
    ppNumber = models.CharField(default=None, blank=True, null=True, max_length=10)


    class Meta:
        db_table = 'Customer'

class Flights(models.Model):
    flightNo = models.CharField(max_length=10,primary_key=True)
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    duration = models.CharField(max_length=5)
    departureTime = models.CharField(max_length=5)
    arrivalTime = models.CharField(max_length=11)
    departureDate = models.DateField()
    price = models.CharField(max_length=5)
    totalSeats = models.IntegerField(default=0)
    newDateFormat = models.CharField(max_length=10)

    class Meta:
        db_table = 'Flights'

class Bookings(models.Model):
    bRef = models.IntegerField(primary_key=True)
    cust = models.ForeignKey(Customer,related_name='cust',on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights,related_name='flight',on_delete=models.CASCADE)
    time = models.DateTimeField()

    class Meta:
        db_table = 'Bookings'
