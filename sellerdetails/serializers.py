from rest_framework import serializers
from .models import sellerDetails

class sellerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sellerDetails
        fields = '__all__'

