# -*- coding: utf-8 -*-
"""
Serializers for publicsafety app
"""
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Arrests, EmergencyPoliceCalls, VictimBasedCrime


class EmergencyPoliceCallsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for EmergencyPoliceCalls
    """
    class Meta:
        """
        Meta for EmergencyPoliceCalls
        """
        model = EmergencyPoliceCalls
        geo_field = "gps_coordinates"
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
                  'gps_coordinates',
                  'census_neighborhoods_2010',
                  'census_wards_precincts',
                  'zip_codes')


class ArrestsSerializer(GeoFeatureModelSerializer):
    """
    Serializer for Arrests
    """
    class Meta:
        """
        Meta for Arrests
        """
        model = Arrests
        geo_field = "gps_coordinates"
        fields = ('arrest_id',
                  'age',
                  'sex',
                  'race',
                  'arrest_date_time',
                  'arrest_date',
                  'arrest_time',
                  'arrest_location',
                  'incident_offense',
                  'incident_location',
                  'charge',
                  'charge_description',
                  'district',
                  'post',
                  'neighborhood',
                  'longitude',
                  'latitude',
                  'gps_coordinates',
                  'location',
                  'census_neighborhoods_2010',
                  'census_wards_precincts',
                  'zip_codes')


class VictimBasedCrimeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for VictimBasedCrime
    """
    class Meta:
        """
        Meta for VictimBasedCrime
        """
        model = VictimBasedCrime
        fields = ('checksum',
                  'crime_date_time',
                  'crime_date',
                  'crime_time',
                  'crime_code',
                  'location',
                  'description',
                  'inside_outside',
                  'weapon',
                  'post',
                  'district',
                  'neighborhood',
                  'longitude',
                  'latitude',
                  'gps_coordinates',
                  'location_1',
                  'premise',
                  'vri_name',
                  'total_incidents')
