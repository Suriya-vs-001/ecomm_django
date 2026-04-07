from rest_framework import viewsets
from .models import UserWishlist
from .serializers import UserWishlistSerializer

class UserWishlistViewSet(viewsets.ModelViewSet):
    queryset = UserWishlist.objects.all()
    serializer_class = UserWishlistSerializer

