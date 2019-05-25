"""
Public safety views
"""
# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .models import EmergencyPoliceCalls
from .serializers import EmergencyPoliceCallsSerializer


class EmergencyPoliceCallsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmergencyPoliceCalls.objects.all()
    serializer_class = EmergencyPoliceCallsSerializer
