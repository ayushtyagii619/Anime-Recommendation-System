from rest_framework import serializers
from .models import NewUser,UserPreferences
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=NewUser.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = NewUser
        fields = ['email','name','password','password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"password field didn't match"})
        return attrs
    def create(self, validated_data):
        user = NewUser.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email  = serializers.CharField(max_length=100)
    class Meta:
        model = NewUser
        fields = ['email','password']
        
class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = ['favorite_genres', 'watched_anime']

class AnimeSearchSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    genre = serializers.CharField(required=False)

class AnimeRecommendationSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    genres = serializers.ListField(child=serializers.CharField())