from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics
from django.db.models import Q
from django.db.models import Count
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView



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
from rest_framework.permissions import AllowAny, IsAuthenticated
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
    permission_classes = [permissions.AllowAny]  # Allows access to anyone
    authentication_classes = []
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
    permission_classes = [permissions.AllowAny]  # Allows access to anyone
    authentication_classes = []
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
    serializer_class = BankDetailSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Return bank details for the authenticated user only
        user = self.request.user
        return BankDetail.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        # Automatically assign the user to the bank detail being created
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Save the bank detail with the user attached
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # Ensure the user can only update their own bank details
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'error': 'You do not have permission to update this bank detail.'}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Ensure the user can only delete their own bank details
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'error': 'You do not have permission to delete this bank detail.'}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    
    def get_queryset(self):
        # Return only the bookings for the authenticated user
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the booking with the authenticated user
        serializer.save(user=self.request.user)


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



class PropertiesByCityView(APIView):

    permission_classes = [permissions.AllowAny]  # Allows access to anyone
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # Aggregate properties by city and count the number of properties in each city
        properties_by_city = Property.objects.values('street__city__name').annotate(
            property_count=Count('id')
        ).order_by('-property_count')  # You can order by count if needed

        # Prepare the response data
        response_data = []
        for item in properties_by_city:
            city_name = item['street__city__name']
            property_count = item['property_count']
            # Add additional city and country information if necessary
            city = City.objects.filter(name=city_name).first()  # Fetch city information
            response_data.append({
                'city': city_name,
                'country': city.country.name if city and city.country else '',
                'property_count': property_count,
                'image_url': f'/assets/cities/{city_name.lower()}.jpg'  # Assuming you store city images in assets
            })

        return Response(response_data)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    #permission_classes = [permissions.AllowAny]  # Allows access to anyone
    #authentication_classes = []

    def get(self, request):
        user = request.user
        if not user.is_authenticated:  # Double-check if the user is authenticated
            raise NotAuthenticated("You must be logged in to view this information.")

        # Serialize user info
        user_data = UserSerializer(user).data

        # Fetch and serialize bank details
        bank_details = BankDetail.objects.filter(user=user)
        bank_data = BankDetailSerializer(bank_details, many=True).data

        # Fetch and serialize bookings
        bookings = Booking.objects.filter(user=user)
        booking_data = BookingSerializer(bookings, many=True).data

        return Response({
            'user_info': user_data,
            'bank_details': bank_data,
            'bookings': booking_data
        })