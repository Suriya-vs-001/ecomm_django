from rest_framework import viewsets
from .models import sellerDetails
from .serializers import sellerDetailsSerializer

class sellerDetailsViewSet(viewsets.ModelViewSet):
    queryset = sellerDetails.objects.all()
    serializer_class = sellerDetailsSerializer

