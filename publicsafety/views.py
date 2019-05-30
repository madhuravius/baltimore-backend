"""
Public safety views
"""
# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .models import Arrests, EmergencyPoliceCalls
from .serializers import EmergencyPoliceCallsSerializer, ArrestsSerializer


class EmergencyPoliceCallsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmergencyPoliceCalls.objects.all()
    serializer_class = EmergencyPoliceCallsSerializer

class ArrestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Arrests.objects.all()
    serializer_class = ArrestsSerializer
