import time
from django.http import JsonResponse
import razorpay
from .clients import get_razorpay_client

def create_order(request):
    """
    View to create a Razorpay order.
    Expected to be called via AJAX/fetch.
    """
    razorpay_client = get_razorpay_client()
    
    # Placeholder for amount logic
    # In a real scenario, fetch this from the cart or product
    final_amount = 0 # Example: 500.00 INR (amount is in paise)

    try:
        # Create order - SYNC call
        order = razorpay_client.order.create({
            "amount": final_amount, 
            "currency": "INR",
            "receipt": f"receipt_{request.user.id}_{int(time.time())}",
            "payment_capture": 1 # Optional: automatic capture
        })
        return JsonResponse(order)
    except Exception as e:
        status_code = getattr(e, 'status_code', 500)
        return JsonResponse({"error": str(e)}, status=status_code)

