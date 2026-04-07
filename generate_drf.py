import os
import django
import sys

# Setup django
sys.path.append('d:/python/Ecommerceproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce_main.settings')
django.setup()

from django.apps import apps
from django.conf import settings

app_names = [
    'base', 'cart', 'content', 'custom_auth', 'offers', 'orders', 
    'payments', 'policy', 'products', 'promotions', 'reviews', 
    'sellerdetails', 'shipping', 'support', 'userdetails', 'wishlist'
]

base_dir = settings.BASE_DIR

for app_name in app_names:
    try:
        app_config = apps.get_app_config(app_name)
        models = app_config.get_models()
        model_names = [model.__name__ for model in models]
        
        app_dir = os.path.join(base_dir, app_name)
        
        # 1. serializers.py
        ser_code = "from rest_framework import serializers\n"
        if model_names:
            ser_code += f"from .models import {', '.join(model_names)}\n\n"
            for m in model_names:
                ser_code += f"class {m}Serializer(serializers.ModelSerializer):\n"
                ser_code += f"    class Meta:\n"
                ser_code += f"        model = {m}\n"
                ser_code += f"        fields = '__all__'\n\n"
        with open(os.path.join(app_dir, 'serializers.py'), 'w') as f:
            f.write(ser_code)
            
        # 2. viewsets
        view_code = "from rest_framework import viewsets\n"
        if model_names:
            view_code += f"from .models import {', '.join(model_names)}\n"
            view_code += f"from .serializers import {', '.join([m+'Serializer' for m in model_names])}\n\n"
            for m in model_names:
                view_code += f"class {m}ViewSet(viewsets.ModelViewSet):\n"
                view_code += f"    queryset = {m}.objects.all()\n"
                view_code += f"    serializer_class = {m}Serializer\n\n"
        with open(os.path.join(app_dir, 'api_viewsets.py'), 'w') as f:
            f.write(view_code)
            
        # 3. urls.py
        url_code = "from django.urls import path, include\n"
        url_code += "from rest_framework.routers import DefaultRouter\n"
        if model_names:
            url_code += f"from .api_viewsets import {', '.join([m+'ViewSet' for m in model_names])}\n\n"
        url_code += "router = DefaultRouter()\n"
        for m in model_names:
            url_code += f"router.register(r'{m.lower()}', {m}ViewSet)\n"
        
        if app_name == 'custom_auth':
            url_code += "\nfrom .api_views import APILoginView, APILogoutView\n"
            url_code += "\nurlpatterns = [\n"
            url_code += "    path('login/', APILoginView.as_view(), name='api_login'),\n"
            url_code += "    path('logout/', APILogoutView.as_view(), name='api_logout'),\n"
            url_code += "    path('', include(router.urls)),\n"
            url_code += "]\n"
        else:
            url_code += "\nurlpatterns = router.urls\n"
            
        with open(os.path.join(app_dir, 'urls.py'), 'w') as f:
            f.write(url_code)
            
        print(f"Generated files for {app_name}")
    except Exception as e:
        print(f"Error for {app_name}: {e}")

# Main URLs
main_urls = """from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
"""
for app_name in app_names:
    main_urls += f"    path('api/v1/{app_name}/', include('{app_name}.urls')),\n"
main_urls += "]\n"
main_urls += "if settings.DEBUG:\n"
main_urls += "    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\n"

with open(os.path.join(base_dir, 'Ecommerce_main', 'urls.py'), 'w') as f:
    f.write(main_urls)

print("Generated APIs successfully")
