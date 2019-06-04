"""
Public safety views
"""
# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .models import Arrests, EmergencyPoliceCalls, VictimBasedCrime
from .serializers import EmergencyPoliceCallsSerializer, \
    ArrestsSerializer, \
    VictimBasedCrimeSerializer


class EmergencyPoliceCallsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows emergency police calls to be viewed or edited.
    """
    queryset = EmergencyPoliceCalls.objects.all()
    serializer_class = EmergencyPoliceCallsSerializer

class ArrestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows arrests to be viewed or edited.
    """
    queryset = Arrests.objects.all()
    serializer_class = ArrestsSerializer


class VictimBasedCrimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows victim-based crime to be viewed or edited.
    """
    queryset = VictimBasedCrime.objects.all()
    serializer_class = VictimBasedCrimeSerializer
