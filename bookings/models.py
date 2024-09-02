from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)


class Meal(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class Continent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True,null=True)


class Street(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,blank=True, null=True)


class PropertyType(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)


class Property(models.Model):
    property_name = models.CharField(max_length=255,blank=True, null=True)
    description = models.CharField(max_length=255,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE,blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE,blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)


class CategoryType(models.Model):
    category = models.CharField(max_length=255,blank=True, null=True)


class Category(models.Model):
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE, related_name='category_type',blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    rating = models.CharField(max_length=10,blank=True, null=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    num = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)


class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to='property_images/',blank=True, null=True)


class Feedback(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    comment = models.CharField(max_length=255,blank=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)


class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    price_p_n = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    amount_of_beds = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=255,blank=True, null=True)
    room_size = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    description = models.CharField(max_length=255,blank=True, null=True)


class RoomFeature(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)


class FeaturesOfRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True)
    room_feature = models.ForeignKey(RoomFeature, on_delete=models.CASCADE,blank=True, null=True)
    is_available = models.BooleanField(default=False,blank=True, null=True)


class PropertyFeature(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)


class FeaturesOfProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,blank=True, null=True)
    property_feature = models.ForeignKey(PropertyFeature, on_delete=models.CASCADE,blank=True, null=True)
    is_available = models.BooleanField(default=False,blank=True, null=True)


class BankDetail(models.Model):
    account_name = models.CharField(max_length=100,blank=True, null=True)
    account_number = models.CharField(max_length=50,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    bank_account = models.ForeignKey(BankDetail, on_delete=models.CASCADE, null=True, blank=True)


class FlightStatus(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)


class FlightType(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)


class Route(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)


class FlightAgency(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)


class Flight(models.Model):
    flight_num = models.CharField(max_length=255,blank=True, null=True)
    seat_no = models.CharField(max_length=255,blank=True, null=True)
    flying_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name="departure_city",blank=True, null=True)
    flying_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name="arrival_city",blank=True, null=True)
    flight_agency = models.ForeignKey(FlightAgency, on_delete=models.CASCADE,blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)


class Price(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,blank=True, null=True)
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE,blank=True, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE,blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)


class BookedFlight(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE,blank=True, null=True)
    final_price = models.ForeignKey(Price, on_delete=models.CASCADE,blank=True, null=True)
    bank_account = models.ForeignKey(BankDetail, on_delete=models.CASCADE,blank=True, null=True)
    flight_status = models.ForeignKey(FlightStatus, on_delete=models.CASCADE,blank=True, null=True)
