from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataEntryViewSet

# Register API routes
router = DefaultRouter()
router.register(r'data', DataEntryViewSet)  # Ensure 'data' is registered

urlpatterns = [
    path('api/', include(router.urls)),  # This registers the API endpoints
]
