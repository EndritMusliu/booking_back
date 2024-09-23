from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserTypeViewSet, UserViewSet, MealViewSet, ContinentViewSet, CountryViewSet, CityViewSet, StreetViewSet,
    PropertyTypeViewSet, PropertyViewSet, CategoryTypeViewSet, CategoryViewSet, RatingViewSet, ImageViewSet,
    FeedbackViewSet, FavoriteViewSet, RoomViewSet, RoomFeatureViewSet, FeaturesOfRoomViewSet,
    PropertyFeatureViewSet, FeaturesOfPropertyViewSet, BankDetailViewSet, BookingViewSet, FlightStatusViewSet,
    FlightTypeViewSet, RouteViewSet, FlightAgencyViewSet, FlightViewSet, PriceViewSet, BookedFlightViewSet, UserCreate,
    LoginView, PropertySearchView, PropertiesByCityView, UserProfileView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'usertypes', UserTypeViewSet)
router.register(r'meals', MealViewSet)
router.register(r'continents', ContinentViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'streets', StreetViewSet)
router.register(r'propertytypes', PropertyTypeViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'categorytypes', CategoryTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'images', ImageViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'roomfeatures', RoomFeatureViewSet)
router.register(r'featuresofroom', FeaturesOfRoomViewSet)
router.register(r'propertyfeatures', PropertyFeatureViewSet)
router.register(r'featuresofproperty', FeaturesOfPropertyViewSet)
router.register(r'bankdetails', BankDetailViewSet,basename='bankdetail')
router.register(r'bookings', BookingViewSet)
router.register(r'flightstatuses', FlightStatusViewSet)
router.register(r'flighttypes', FlightTypeViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'flightagencies', FlightAgencyViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'bookedflights', BookedFlightViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('api/properties/search/', PropertySearchView.as_view(), name='property-search'),
    path('properties-by-city/', PropertiesByCityView.as_view(), name='properties-by-city'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

]
