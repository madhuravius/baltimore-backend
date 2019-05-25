"""
Models for publicsafety app
"""
# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


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
    census_neighborhoods_2010 = models.TextField()  # 2010 Census Neighborhoods
    census_wards_precincts = models.TextField()  # 2010 Census Wards Precincts
    zip_codes = models.TextField()  # Zip Codes

    class Meta:
        ordering = ['-record_id']

    def insert_from_csv(self, line):
        """
        Helper method to create entry from a single line provided in a csv
        """
        entry = EmergencyPoliceCalls(
            record_id=line[0],
            call_number=line[1],
            call_date_time=datetime.strptime(
                line[2], '%m/%d/%Y %H:%M:%S %p'),
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
            census_neighborhoods_2010=line[17],
            census_wards_precincts=line[18],
            zip_codes=line[19],
        )
        entry.save()

    def __str__(self):
        return self.record_id
