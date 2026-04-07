from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import sellerDetailsViewSet

router = DefaultRouter()
router.register(r'sellerdetails', sellerDetailsViewSet)

urlpatterns = router.urls
