# Ensure the URLs in custom_auth are correctly defined
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    # Define your custom_auth URLs here
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('user_validation/', views.user_validation, name="user_validation"),
    path('user_registration/', views.user_registration, name="user_registration"),
    path('user_exist_validator_with_email/', views.user_exist_validator_with_email, name="user_exist_validator_with_email"),

    # Add a direct reset password URL
    path('reset-password/<int:user_id>/', views.reset_password, name="reset_password"),

    # Password reset URLs
    path('password_regenerate/', views.CustomPasswordResetView.as_view(), name="password_regenerate"),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
