from django.urls import path
from . import views

urlpatterns = [
    path('tos/', views.terms, name="tos"),
    path('privacy/', views.privacyPolicy, name="privacy"),
    path('return-policy/', views.returnPolicy, name="return-policy"),
    path('support/', views.support, name="support"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
]
