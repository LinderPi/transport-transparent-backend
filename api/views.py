from rest_framework import permissions, viewsets
from .models import Company, CsvFile
from .serializers import CompanySerializer, CsvFileSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

class CsvFileViewSet(viewsets.ModelViewSet):
    queryset = CsvFile.objects.all()
    serializer_class = CsvFileSerializer
    permission_classes = [permissions.AllowAny]
