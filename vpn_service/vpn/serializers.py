from rest_framework import serializers
from .models import UserSite
from users.models import UserProfile

class UserSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSite
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
