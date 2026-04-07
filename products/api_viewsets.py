from rest_framework import viewsets
from .models import newproduct
from .serializers import newproductSerializer

class newproductViewSet(viewsets.ModelViewSet):
    queryset = newproduct.objects.all()
    serializer_class = newproductSerializer

