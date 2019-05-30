# -*- coding: utf-8 -*-
"""
Constants for util
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baltimore.settings')
APPLICATION = get_wsgi_application()

from publicsafety import models #pylint: disable=wrong-import-position

DOWNLOAD_PATH = './raw/'

# Starting section of field column names on csvs
MAPPING_911_POLICE_CALLS = {
    'fields': ['RecordID',
               'CallNumber',
               'CallDateTime',
               'Priority',
               'District',
               'Description',
               'IncidentLocation',
               'ZipCode',
               'Neighborhood',
               'PoliceDistrict',
               'PolicePost',
               'CouncilDistrict',
               'SheriffDistricts',
               'Community_Statistical_Areas',
               'Census_Tracts',
               'VRIZones',
               'Location',
               '2010 Census Neighborhoods',
               '2010 Census Wards Precincts',
               'Zip Codes']
}

MAPPING_BPD_ARRESTS = {
    'fields': ['Arrest',
               'Age',
               'Sex',
               'Race',
               'ArrestDate',
               'ArrestTime',
               'ArrestLocation',
               'IncidentOffense',
               'IncidentLocation',
               'Charge',
               'ChargeDescription',
               'District',
               'Post',
               'Neighborhood',
               'Longitude',
               'Latitude',
               'Location 1',
               '2010 Census Neighborhoods',
               '2010 Census Wards Precincts',
               'Zip Codes']
}


MAPPING_BPD_VICTIM_BASED_CRIMES = {
    'fields': ['CrimeDate',
               'CrimeTime',
               'CrimeCode',
               'Location',
               'Description',
               'Inside/Outside',
               'Weapon',
               'Post',
               'District',
               'Neighborhood',
               'Longitude',
               'Latitude',
               'Location 1',
               'Premise',
               'vri_name1',
               'Total Incidents']
}

MAPPING_GUN_OFFENDERS = {
    'fields': ['caseNumber',
               'created_date',
               'modified_date',
               'lastName',
               'firstName',
               'middleName',
               'Date_Of_Birth',
               'sex',
               'race',
               'full_address',
               'city',
               'state',
               'zip_code',
               'district',
               'post',
               'neighborhood',
               'Longitude',
               'Latitude',
               'Location 1']
}

MAPPING_USE_OF_FORCE = {
    'fields': ['DATE',
               'CC#',
               'DISTRICT',
               'LOCATION',
               'TYPE',
               'X (LONG)',
               'Y (LAT)',
               'COORDINATES',
               'Zip Codes']
}

FILE_PARENT_MAPPING = [
    {
        'readable_name': '911 Police Calls For Service',
        'file_name': '911_Police_Calls_for_Service.csv',
        'url': 'https://data.baltimorecity.gov/api/views/m8g9-abgb/rows.csv?accessType=DOWNLOAD',
        'mapping': MAPPING_911_POLICE_CALLS,
        'model': models.EmergencyPoliceCalls,
    },
    {
        'readable_name': 'BPD Arrests',
        'file_name': 'BPD_Arrests.csv',
        'url': 'https://data.baltimorecity.gov/api/views/3i3v-ibrt/rows.csv?accessType=DOWNLOAD',
        'mapping': MAPPING_BPD_ARRESTS,
    },  # below might need
    {
        'readable_name': 'BPD Victim Based Crime Data',
        'file_name': 'BPD_Part_1_Victim_Based_Crime_Data.csv',
        'url': 'https://data.baltimorecity.gov/api/views/wsfq-mvij/rows.csv?accessType=DOWNLOAD',
        'mapping': MAPPING_BPD_ARRESTS,
    },
    {
        'readable_name': 'Gun Offenders',
        'file_name': 'Gun_Offenders.csv',
        'url': 'https://data.baltimorecity.gov/api/views/aivj-4x23/rows.csv?accessType=DOWNLOAD',
        'mapping': MAPPING_GUN_OFFENDERS,
    },
    {
        'readable_name': 'Police Use of Force and In-Custody Injuries',
        'file_name': 'Police_use_of_force_and_in-custody_injuries.csv',
        'url': 'https://data.baltimorecity.gov/api/views/5kep-c625/rows.csv?accessType=DOWNLOAD',
        'mapping': MAPPING_USE_OF_FORCE,
    }
]

BALTIMORE_SHAPEFILE_URL = 'https://data.baltimorecity.gov/api/geospatial/27b4-qbwn' + \
    '?method=export&format=Shapefile'
BALTIMORE_SHAPEFILE_LOCATION = "baltimore.zip"
