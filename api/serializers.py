from rest_framework import serializers
from .models import Company, Route

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'routes']

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'start', 'end', 'distance', 'duration', 'quantity', 'transportation', 'delivery',
                  'energy_goods', 'frequency']
