# -*- coding: utf-8 -*-
"""
Serializers for publicsafety app
"""
from rest_framework import serializers
from .models import EmergencyPoliceCalls


class EmergencyPoliceCallsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for EmergencyPoliceCalls
    """
    class Meta:
        """
        Meta for EmergencyPoliceCalls
        """
        model = EmergencyPoliceCalls
        fields = ('record_id',
                  'call_number',
                  'call_date_time',
                  'priority',
                  'district',
                  'description',
                  'incident_location',
                  'zipcode',
                  'neighborhood',
                  'police_district',
                  'police_post',
                  'council_district',
                  'sheriff_districts',
                  'community_statistical_areas',
                  'census_tracts',
                  'vri_zones',
                  'location',
                  'census_neighborhoods_2010',
                  'census_wards_precincts',
                  'zip_codes')
