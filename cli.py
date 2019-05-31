# -*- coding: utf-8 -*-
"""
Command line utility
"""
import zipfile

import click

from util import constants
from util import dbimport
from util import util

@click.group()
def main():
    """
    Simple CLI for downloading baltimore police data
    """
    click.echo("")


@main.command()
def download():
    """
    -- 💾  Download all raw files
    """
    click.echo("💾  - Downloading all raw files")
    util.download_all_raw_data()


@main.command()
def database():
    """
    -- 🤖 Import all raw files to database
        * - All (USE WITH CAUTION)
        Public Safety
        1. 911 Police Calls For Service
        2. BPD Arrests
        3. BPD Victim Based Crime Data
        4. Gun Offenders
        5. Police Use of Force and In-Custody Injuries
    """
    click.echo("🤖  - Importing raw files to database")
    filename = constants.DOWNLOAD_PATH + \
        constants.FILE_PARENT_MAPPING[2]['file_name']
    dbimport.import_data_to_db(
        filename, constants.FILE_PARENT_MAPPING[2]['model'])

@main.command()
def shapefiles():
    """
    -- 🗺 Import all shape files to raw
    """
    click.echo("🗺  - Importing raw files to database")
    util.download_file(constants.BALTIMORE_SHAPEFILE_URL, constants.BALTIMORE_SHAPEFILE_LOCATION)
    zip_ref = zipfile.ZipFile(constants.DOWNLOAD_PATH + constants.BALTIMORE_SHAPEFILE_LOCATION, 'r')
    zip_ref.extractall(constants.DOWNLOAD_PATH)


@main.command()
def start():
    """
    -- 🎆 Start application locally
    """
    click.echo("🎆  - Starting application")


if __name__ == "__main__":
    main()
