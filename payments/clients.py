import razorpay
from razorpay import Client
from django.conf import settings

def get_razorpay_client():
    return Client(
        api_key=settings.RAZORPAY_API_KEY,
        api_secret=settings.RAZORPAY_API_SECRET,
    )   

# deals in loading the payment secret details.