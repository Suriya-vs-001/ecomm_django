from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import UserPaymentCardViewSet

router = DefaultRouter()
router.register(r'userpaymentcard', UserPaymentCardViewSet)

urlpatterns = router.urls
