from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from .api_views import APILoginView, APILogoutView

urlpatterns = [
    path('login/', APILoginView.as_view(), name='api_login'),
    path('logout/', APILogoutView.as_view(), name='api_logout'),
    path('', include(router.urls)),
    path('password_regenerate/', views.CustomPasswordResetView.as_view(), name="password_regenerate"),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
]
