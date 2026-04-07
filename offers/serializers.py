from rest_framework import serializers
from .models import PersonalizedDeal

class PersonalizedDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedDeal
        fields = '__all__'

