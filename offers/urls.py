from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import PersonalizedDealViewSet

router = DefaultRouter()
router.register(r'personalizeddeal', PersonalizedDealViewSet)

urlpatterns = router.urls
