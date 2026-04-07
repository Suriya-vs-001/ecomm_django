from rest_framework import viewsets
from .models import UserPaymentCard
from .serializers import UserPaymentCardSerializer

class UserPaymentCardViewSet(viewsets.ModelViewSet):
    queryset = UserPaymentCard.objects.all()
    serializer_class = UserPaymentCardSerializer

