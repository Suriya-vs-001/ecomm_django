from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import UserOrderViewSet, OrderItemViewSet, OrderStatusHistoryViewSet

router = DefaultRouter()
router.register(r'userorder', UserOrderViewSet)
router.register(r'orderitem', OrderItemViewSet)
router.register(r'orderstatushistory', OrderStatusHistoryViewSet)

urlpatterns = router.urls
