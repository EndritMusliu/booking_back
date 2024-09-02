from rest_framework.authtoken.models import Token
# Register your models here.




from .models import (
    UserType, User, Meal, Continent, Country, City, Street, PropertyType, Property,
    CategoryType, Category, Rating, Image, Feedback, Favorite, Room, RoomFeature,
    FeaturesOfRoom, PropertyFeature, FeaturesOfProperty, BankDetail, Booking,
    FlightStatus, FlightType, Route, FlightAgency, Flight, Price, BookedFlight
)

# Registering all models to the admin site
admin.site.register(Token)
admin.site.register(UserType)
admin.site.register(User)
admin.site.register(Meal)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Image)
admin.site.register(Feedback)
admin.site.register(Favorite)
admin.site.register(Room)
admin.site.register(RoomFeature)
admin.site.register(FeaturesOfRoom)
admin.site.register(PropertyFeature)
admin.site.register(FeaturesOfProperty)
admin.site.register(BankDetail)
admin.site.register(Booking)
admin.site.register(FlightStatus)
admin.site.register(FlightType)
admin.site.register(Route)
admin.site.register(FlightAgency)
admin.site.register(Flight)
admin.site.register(Price)
admin.site.register(BookedFlight)