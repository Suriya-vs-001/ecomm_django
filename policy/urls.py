from django.urls import path
from . import views

urlpatterns = [
    path('tos/', views.TermsView.as_view(), name="tos"),
    path('privacy/', views.PrivacyPolicyView.as_view(), name="privacy"),
    path('return-policy/', views.ReturnPolicyView.as_view(), name="return-policy"),
    path('support/', views.SupportView.as_view(), name="support"),
    path('faq/', views.FAQView.as_view(), name="faq"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
