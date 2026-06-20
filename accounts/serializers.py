from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "id", "full_name", "email"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = ["full_name", "email", "password"]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["email"],
            full_name=validated_data["full_name"],
            email=validated_data["email"],
            password=validated_data["password"]
            )
        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"