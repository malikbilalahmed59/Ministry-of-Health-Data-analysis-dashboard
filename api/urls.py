from django.urls import path
from rest_framework import routers
from rest_framework_nested import routers

from rest_framework.routers import DefaultRouter
from . import views

router = routers.DefaultRouter()
router.register('Division', views.DivisionViewSet)

district_routers = routers.NestedDefaultRouter(router, 'Division', lookup="division")
district_routers.register('district', views.DistrictViewSet, basename="division-district")


urlpatterns = router.urls + district_routers.urls
