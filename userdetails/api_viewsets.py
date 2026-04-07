from rest_framework import viewsets
from .models import UserDetails, UserInformation, UserPreferences, UserSearchHistory, UserActivity
from .serializers import UserDetailsSerializer, UserInformationSerializer, UserPreferencesSerializer, UserSearchHistorySerializer, UserActivitySerializer

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer

class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer

class UserSearchHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserSearchHistory.objects.all()
    serializer_class = UserSearchHistorySerializer

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

