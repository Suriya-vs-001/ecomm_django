from rest_framework import viewsets
from .models import PersonalizedDeal
from .serializers import PersonalizedDealSerializer

class PersonalizedDealViewSet(viewsets.ModelViewSet):
    queryset = PersonalizedDeal.objects.all()
    serializer_class = PersonalizedDealSerializer

