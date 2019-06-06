"""
Public safety views
"""
# -*- coding: utf-8 -*-

from django.contrib.gis.geos import Point
from rest_framework import viewsets

from .models import Arrests, EmergencyPoliceCalls, VictimBasedCrime
from .serializers import EmergencyPoliceCallsSerializer, \
    ArrestsSerializer, \
    VictimBasedCrimeSerializer
from .utils import get_map_locations, get_start_date_end_date_params


EMERGENCY_POLICE_CALLS_BASE_QUERYSET = EmergencyPoliceCalls.objects.all()
ARRESTS_BASE_QUERYSET = Arrests.objects.all()
VICTIM_BASED_CRIME_BASE_QUERYSET = VictimBasedCrime.objects.all()

class EmergencyPoliceCallsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows emergency police calls to be viewed or edited.
    """
    queryset = EMERGENCY_POLICE_CALLS_BASE_QUERYSET
    serializer_class = EmergencyPoliceCallsSerializer

    def get_queryset(self):
        # optionally filter by start/end date
        queryset = EMERGENCY_POLICE_CALLS_BASE_QUERYSET
        start_date, end_date = get_start_date_end_date_params(self.request)
        if start_date and end_date:
            queryset = queryset.filter(
                call_date_time__gte=start_date,
                call_date_time__lte=end_date)
        if get_map_locations(self.request):
            queryset = queryset.exclude(gps_coordinates__intersects=Point(0.0, 0.0))
        return queryset


class ArrestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows arrests to be viewed or edited.
    """
    queryset = ARRESTS_BASE_QUERYSET
    serializer_class = ArrestsSerializer

    def get_queryset(self):
        # optionally filter by start/end date
        queryset = ARRESTS_BASE_QUERYSET
        start_date, end_date = get_start_date_end_date_params(self.request)
        if start_date and end_date:
            queryset = queryset.filter(
                arrest_date_time__gte=start_date,
                arrest_date_time__lte=end_date)
        if get_map_locations(self.request):
            queryset = queryset.exclude(gps_coordinates__intersects=Point(0.0, 0.0))
        return queryset


class VictimBasedCrimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows victim-based crime to be viewed or edited.
    """
    queryset = VICTIM_BASED_CRIME_BASE_QUERYSET
    serializer_class = VictimBasedCrimeSerializer

    def get_queryset(self):
        # optionally filter by start/end date
        queryset = VICTIM_BASED_CRIME_BASE_QUERYSET
        start_date, end_date = get_start_date_end_date_params(self.request)
        if start_date and end_date:
            queryset = queryset.filter(
                crime_date_time__gte=start_date,
                crime_date_time__lte=end_date)
        if get_map_locations(self.request):
            queryset = queryset.exclude(gps_coordinates__intersects=Point(0.0, 0.0))
        return queryset
