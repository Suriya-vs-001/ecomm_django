from rest_framework import serializers
from .models import UserWishlist

class UserWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWishlist
        fields = '__all__'

