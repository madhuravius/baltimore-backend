"""
Models for publicsafety app
"""
# -*- coding: utf-8 -*-

from datetime import datetime
import re

from django.db import models
from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point


class EmergencyPoliceCalls(models.Model):
    """
    Maps to this file dump: 911_Police_Calls_for_Service.csv (see FILE_PARENT_MAPPING)
    Sample result
    line[1] = ['2', 'P190531375', '02/22/2019 10:08:00 AM', 'Non-Emergency', 'WD',
    'Hot Spot Check', '1600 BLK N SMALLWOOD ST', '21216', 'Coppin Heights/Ash-Co-East',
    'Western', '723', '7', 'D9', 'Greater Rosemont', 'Census Tract 1503', 'Western',
    '1600 BLK N SMALLWOOD ST\nBALTIMORE, MD', '', '', '']
    """
    record_id = models.CharField(max_length=100, primary_key=True)  # RecordID
    call_number = models.CharField(max_length=100)  # CallNumber
    call_date_time = models.DateTimeField(db_index=True)  # CallDateTime
    priority = models.CharField(max_length=30)  # Priority
    district = models.CharField(max_length=10)  # District
    description = models.TextField()  # Description
    incident_location = models.TextField()  # IncidentLocation
    zipcode = models.CharField(max_length=10)  # ZipCode
    neighborhood = models.CharField(max_length=100)  # Neighborhood
    police_district = models.CharField(max_length=30)  # PoliceDistrict
    police_post = models.CharField(max_length=10)  # PolicePost
    council_district = models.IntegerField()  # CouncilDistrict
    sheriff_districts = models.CharField(max_length=20)  # SheriffDistricts
    community_statistical_areas = models.TextField()  # Community_Statistical_Areas
    census_tracts = models.TextField()  # Census_Tracts
    vri_zones = models.CharField(max_length=100)  # VRIZones
    location = models.TextField()  # Location
    gps_coordinates = geo_models.PointField() # Derived from location (regex parse)
    census_neighborhoods_2010 = models.TextField()  # 2010 Census Neighborhoods
    census_wards_precincts = models.TextField()  # 2010 Census Wards Precincts
    zip_codes = models.TextField()  # Zip Codes

    class Meta:
        ordering = ['-record_id']

    def insert_from_csv(self, line):
        """
        Helper method to create entry from a single line provided in a csv
        """
        # find contents only inside of parens for gps and use it for point field
        regex_pattern = r'.()([-+]?)([\d]{1,2})(((\.)(\d+)(,)))(\s*)(([-+]?)([\d]{1,3})((\.)(\d+))?(\)))$' #pylint: disable=line-too-long
        gps_coordinates_raw = re.search(regex_pattern, line[16])

        if hasattr(gps_coordinates_raw, 'group'):
            gps_coordinates = gps_coordinates_raw.group(0)
            gps_coordinates = gps_coordinates.replace('(', '').replace(')', '').split(',')
            gps_coordinates = [float(elem) for elem in gps_coordinates]
        else:
            gps_coordinates = [None, None]

        entry = EmergencyPoliceCalls(
            record_id=line[0],
            call_number=line[1],
            call_date_time=datetime.strptime(
                line[2], '%m/%d/%Y %I:%M:%S %p'),
            priority=line[3],
            district=line[4],
            description=line[5],
            incident_location=line[6],
            zipcode=line[7],
            neighborhood=line[8],
            police_district=line[9],
            police_post=line[10],
            council_district=line[11] or 0,
            sheriff_districts=line[12],
            community_statistical_areas=line[13],
            census_tracts=line[14],
            vri_zones=line[15],
            location=line[16],
            gps_coordinates=Point(gps_coordinates[0], gps_coordinates[1]),
            census_neighborhoods_2010=line[17],
            census_wards_precincts=line[18],
            zip_codes=line[19],
        )
        entry.save()

    def __str__(self):
        return self.record_id

class Arrests(models.Model):
    '''
    Generated from following dump:
    Arrest,Age,Sex,Race,ArrestDate,ArrestTime,ArrestLocation,IncidentOffense,IncidentLocation,Charge,ChargeDescription,District,Post,Neighborhood,Longitude,Latitude,Location 1,2010 Census Neighborhoods,2010 Census Wards Precincts,Zip Codes #pylint: disable=line-too-long
    Sample record:
    19030389,21,M,B,02/28/2019,11:45,1 SMALLWOOD ST,Unknown Offense,1 SMALLWOOD ST,1 1111,CDS V IOLATION,Southwest,835,,-76.651425000000,39.287927000000,,,,
    OR another example
    19030722,28,F,W,02/28/2019,15:04,,Unknown Offense,,1 1137,THEFT: $100 TO UNDER $1,500,,,,,,,,
    '''
    arrest_id = models.CharField(max_length=100, primary_key=True) # Arrest
    age = models.IntegerField() # Age
    sex = models.CharField(max_length=10) # Sex
    race = models.CharField(max_length=10) # Race
    arrest_date_time = models.DateTimeField(db_index=True)  # derived from ArrestDate and ArrestTime
    arrest_date = models.DateField() # ArrestDate
    arrest_time = models.TimeField() # ArrestTime
    arrest_location = models.TextField()  # ArrestLocation
    incident_offense = models.CharField(max_length=100) # IncidentOffense
    incident_location = models.TextField()  # IncidentLocation
    charge = models.CharField(max_length=100) # Charge
    charge_description = models.TextField()  # ChargeDescription
    district = models.CharField(max_length=30)  # District
    post = models.CharField(max_length=10)  # Post
    neighborhood = models.CharField(max_length=100)  # Neighborhood
    longitude = models.FloatField() # Longitude
    latitude = models.FloatField() # Latitude
    gps_coordinates = geo_models.PointField() # Derived from latitude and longitude
    location = models.TextField()  # Location 1
    census_neighborhoods_2010 = models.TextField()  # 2010 Census Neighborhoods
    census_wards_precincts = models.TextField()  # 2010 Census Wards Precincts
    zip_codes = models.TextField()  # Zip Codes

    class Meta:
        ordering = ['-arrest_id']
