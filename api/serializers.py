from rest_framework import serializers
from .models import Company, Route

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'routes']

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'delivery', 'start', 'end', 'product', 'quantity', 'duration_max', 'distance_train',
                  'duration_train', 'energy_train', 'distance_truck', 'duration_truck', 'energy_truck', 'distance_ship',
                  'duration_ship', 'energy_ship', 'distance_plane', 'duration_plane', 'energy_plane', 'distance_bike',
                  'duration_bike', 'energy_bike', 'name_others', 'distance_others', 'duration_others', 'energy_others',
                  'energy_goods', 'emissions']
