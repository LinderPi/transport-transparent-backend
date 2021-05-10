from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'route', views.RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
