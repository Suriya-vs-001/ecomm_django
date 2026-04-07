from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import UserDetailsViewSet, UserInformationViewSet, UserPreferencesViewSet, UserSearchHistoryViewSet, UserActivityViewSet

router = DefaultRouter()
router.register(r'userdetails', UserDetailsViewSet)
router.register(r'userinformation', UserInformationViewSet)
router.register(r'userpreferences', UserPreferencesViewSet)
router.register(r'usersearchhistory', UserSearchHistoryViewSet)
router.register(r'useractivity', UserActivityViewSet)

urlpatterns = router.urls
