from django.urls import path, include
from restapi.views import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"employee", EmployeeViewSet, basename='employee')

urlpatterns = [path("", include(router.urls))]
