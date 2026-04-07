from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base/', include('base.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/custom_auth/', include('custom_auth.urls')),
    path('api/v1/offers/', include('offers.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/payments/', include('payments.urls')),
    path('api/v1/policy/', include('policy.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/promotions/', include('promotions.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/sellerdetails/', include('sellerdetails.urls')),
    path('api/v1/shipping/', include('shipping.urls')),
    path('api/v1/support/', include('support.urls')),
    path('api/v1/userdetails/', include('userdetails.urls')),
    path('api/v1/wishlist/', include('wishlist.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
