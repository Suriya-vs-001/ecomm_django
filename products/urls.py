from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import newproductViewSet

router = DefaultRouter()
router.register(r'newproduct', newproductViewSet)

urlpatterns = router.urls
