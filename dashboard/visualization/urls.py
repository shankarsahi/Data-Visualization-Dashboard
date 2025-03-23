# Step 6: Register API Routes
## Update `urls.py` inside `visualization` app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from visualization.views import DataPointViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'data', DataPointViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from visualization.views import DataPointViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'data', DataPointViewSet, basename='datapoint')

urlpatterns = [
    path('', include(router.urls)),  # Ensure this is included
]
