from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from visualization.models import DataPoint
from visualization.serializers import DataPointSerializer

class DataPointViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows data points to be viewed.
    Supports filtering by year, country, topics, region, and city.
    """
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year')
        country = self.request.query_params.get('country')
        topics = self.request.query_params.get('topics')
        region = self.request.query_params.get('region')
        city = self.request.query_params.get('city')
        
        if year:
            queryset = queryset.filter(year=year)
        if country:
            queryset = queryset.filter(country__icontains=country)
        if topics:
            queryset = queryset.filter(topics__icontains=topics)
        if region:
            queryset = queryset.filter(region__icontains=region)
        if city:
            queryset = queryset.filter(city__icontains=city)
        
        return queryset