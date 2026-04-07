from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import UserWishlistViewSet

router = DefaultRouter()
router.register(r'userwishlist', UserWishlistViewSet)

urlpatterns = router.urls
