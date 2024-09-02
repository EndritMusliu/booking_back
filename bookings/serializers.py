from django.contrib.auth import authenticate
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import (
    UserType, User, Meal, Continent, Country, City, Street, PropertyType, Property,
    CategoryType, Category, Rating, Image, Feedback, Favorite, Room, RoomFeature,
    FeaturesOfRoom, PropertyFeature, FeaturesOfProperty, BankDetail, Booking,
    FlightStatus, FlightType, Route, FlightAgency, Flight, Price, BookedFlight
)


from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        Token.objects.create(user=user)  # Automatically create a token for the user
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User account is disabled."
                    raise serializers.ValidationError(msg)
            else:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg)
        else:
            msg = "Must include both username and password."
            raise serializers.ValidationError(msg)
        return data



class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class UserSerializer(WritableNestedModelSerializer):
    user_type = UserTypeSerializer(allow_null=True, required=False)

    class Meta:
        model = User
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'


class CountrySerializer(WritableNestedModelSerializer):
    continent = ContinentSerializer(allow_null=True, required=False)

    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(WritableNestedModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(WritableNestedModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'


class PropertySerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property_type = PropertyTypeSerializer()
    street = StreetSerializer()
    meal = MealSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = '__all__'


class CategorySerializer(WritableNestedModelSerializer):
    category_type = CategoryTypeSerializer()
    property = PropertySerializer()

    class Meta:
        model = Category
        fields = '__all__'


class RatingSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property = PropertySerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class ImageSerializer(WritableNestedModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = Image
        fields = '__all__'


class FeedbackSerializer(WritableNestedModelSerializer):
    property = PropertySerializer()
    user = UserSerializer()

    class Meta:
        model = Feedback
        fields = '__all__'


class FavoriteSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property = PropertySerializer()

    class Meta:
        model = Favorite
        fields = '__all__'


class RoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFeature
        fields = '__all__'


class FeaturesOfRoomSerializer(WritableNestedModelSerializer):
    room_feature = RoomFeatureSerializer()

    class Meta:
        model = FeaturesOfRoom
        fields = '__all__'


class RoomSerializer(WritableNestedModelSerializer):
    property = PropertySerializer()
    features_of_room = FeaturesOfRoomSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'


class PropertyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFeature
        fields = '__all__'


class FeaturesOfPropertySerializer(WritableNestedModelSerializer):
    property_feature = PropertyFeatureSerializer()

    class Meta:
        model = FeaturesOfProperty
        fields = '__all__'


class BankDetailSerializer(WritableNestedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BankDetail
        fields = '__all__'


class BookingSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    room = RoomSerializer()
    bank_account = BankDetailSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class FlightStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightStatus
        fields = '__all__'


class FlightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightType
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class FlightAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightAgency
        fields = '__all__'


class FlightSerializer(WritableNestedModelSerializer):
    flying_from = CitySerializer()
    flying_to = CitySerializer()
    flight_agency = FlightAgencySerializer()

    class Meta:
        model = Flight
        fields = '__all__'


class PriceSerializer(WritableNestedModelSerializer):
    flight = FlightSerializer()
    flight_type = FlightTypeSerializer()
    route = RouteSerializer()

    class Meta:
        model = Price
        fields = '__all__'


class BookedFlightSerializer(WritableNestedModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()
    route = RouteSerializer()
    final_price = PriceSerializer()
    bank_account = BankDetailSerializer()
    flight_status = FlightStatusSerializer()

    class Meta:
        model = BookedFlight
        fields = '__all__'
