from rest_framework import serializers
from .models import newproduct

class newproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = newproduct
        fields = '__all__'

