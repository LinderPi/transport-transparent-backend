from rest_framework import serializers
from .models import Company, CsvFile

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'tonnage', 'distance_train', 'distance_truck', 'distance_ship', 'distance_plane',
                  'distance_bike', 'distance_others', 'transports_per_day', 'short_term']

class CsvFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CsvFile
        fields = ['id', 'upload_time', 'file']
