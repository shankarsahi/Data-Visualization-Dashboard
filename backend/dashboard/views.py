from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import DataEntry
from .serializers import DataEntrySerializer

class DataEntryViewSet(viewsets.ModelViewSet):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['end_year', 'topic', 'sector', 'region', 'pestle', 'source', 'country', 'city']
    search_fields = ['title', 'insight']
    ordering_fields = ['intensity', 'relevance', 'likelihood']


from django.core.cache import cache

class CachedDataEntryViewSet(viewsets.ModelViewSet):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "data_entries"
        data = cache.get(cache_key)
        if not data:
            data = super().list(request, *args, **kwargs)
            cache.set(cache_key, data, timeout=60*5)  # Cache for 5 minutes
        return data


from rest_framework import viewsets
from .models import DataEntry
from .serializers import DataEntrySerializer

class DataEntryViewSet(viewsets.ModelViewSet):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer
