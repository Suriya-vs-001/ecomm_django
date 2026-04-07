from rest_framework import viewsets
from .models import UserReview
from .serializers import UserReviewSerializer

class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer

