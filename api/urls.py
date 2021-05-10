from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
