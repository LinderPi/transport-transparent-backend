from rest_framework import serializers
from .models import Company, CsvFile

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'tonnage', 'distance']

class CsvFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CsvFile
        fields = ['id', 'upload_time', 'file']
