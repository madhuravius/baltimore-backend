# -*- coding: utf-8 -*-
"""
Urls for baltimore project
"""
from django.urls import include, path
from rest_framework import routers
from publicsafety import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'api/v1/publicsafety/emergencypolicecalls',
                views.EmergencyPoliceCallsViewSet)
ROUTER.register(r'api/v1/publicsafety/arrests',
                views.ArrestsViewSet)
ROUTER.register(r'api/v1/publicsafety/victimbasedcrime',
                views.VictimBasedCrimeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
