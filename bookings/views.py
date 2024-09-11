from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics
from django.db.models import Q

from .models import (
    UserType, User, Meal, Continent, Country, City, Street, PropertyType, Property,
    CategoryType, Category, Rating, Image, Feedback, Favorite, Room, RoomFeature,
    FeaturesOfRoom, PropertyFeature, FeaturesOfProperty, BankDetail, Booking,
    FlightStatus, FlightType, Route, FlightAgency, Flight, Price, BookedFlight
)
from .serializers import (
    UserTypeSerializer, UserSerializer, MealSerializer, ContinentSerializer, CountrySerializer,
    CitySerializer, StreetSerializer, PropertyTypeSerializer, PropertySerializer, CategoryTypeSerializer,
    CategorySerializer, RatingSerializer, ImageSerializer, FeedbackSerializer, FavoriteSerializer,
    RoomSerializer, RoomFeatureSerializer, FeaturesOfRoomSerializer, PropertyFeatureSerializer,
    FeaturesOfPropertySerializer, BankDetailSerializer, BookingSerializer, FlightStatusSerializer,
    FlightTypeSerializer, RouteSerializer, FlightAgencySerializer, FlightSerializer, PriceSerializer,
    BookedFlightSerializer
)


from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status,views, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model


class UserCreate(views.APIView):
    permission_classes = [permissions.AllowAny]  # Allows access to anyone
    authentication_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]  # Allows access to anyone
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.select_related('user', 'property_type', 'street__city__country', 'meal').all()


        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(property_name__icontains=search_query)

        return queryset






class ContinentViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomFeatureViewSet(viewsets.ModelViewSet):
    queryset = RoomFeature.objects.all()
    serializer_class = RoomFeatureSerializer


class FeaturesOfRoomViewSet(viewsets.ModelViewSet):
    queryset = FeaturesOfRoom.objects.all()
    serializer_class = FeaturesOfRoomSerializer


class PropertyFeatureViewSet(viewsets.ModelViewSet):
    queryset = PropertyFeature.objects.all()
    serializer_class = PropertyFeatureSerializer


class FeaturesOfPropertyViewSet(viewsets.ModelViewSet):
    queryset = FeaturesOfProperty.objects.all()
    serializer_class = FeaturesOfPropertySerializer


class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class FlightStatusViewSet(viewsets.ModelViewSet):
    queryset = FlightStatus.objects.all()
    serializer_class = FlightStatusSerializer


class FlightTypeViewSet(viewsets.ModelViewSet):
    queryset = FlightType.objects.all()
    serializer_class = FlightTypeSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class FlightAgencyViewSet(viewsets.ModelViewSet):
    queryset = FlightAgency.objects.all()
    serializer_class = FlightAgencySerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class BookedFlightViewSet(viewsets.ModelViewSet):
    queryset = BookedFlight.objects.all()
    serializer_class = BookedFlightSerializer
