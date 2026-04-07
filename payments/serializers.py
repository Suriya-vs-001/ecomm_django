from rest_framework import serializers
from .models import UserPaymentCard

class UserPaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPaymentCard
        fields = '__all__'

