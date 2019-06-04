# -*- coding: utf-8 -*-
"""
Command line utility
"""
import zipfile

import click
from yaspin import yaspin

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
@click.option('--selection', help="Select a ")
def database(selection):
    """
    -- 🤖 Import all raw files to database
    """
    if not selection:
        print("""You must choose a selection. Choose a file selection (or import all with '*'):

all - All (USE WITH CAUTION)
================================
    Public Safety
1 - 911 Police Calls For Service
2 - BPD Arrests
3 - BPD Victim Based Crime Data
4 - Gun Offenders
5 - Police Use of Force and In-Custody Injuries
6 - Homicide Data (Washington Post)
""")
    elif selection == "All" or (selection != "all" and selection.isnumeric()):
        click.echo("🤖  - Importing raw files to database")
        click.echo("You chose a selection: %s" % selection)

        filtered_selection = constants.FILE_PARENT_MAPPING
        if selection.isnumeric():
            filtered_selection = [filtered_selection[int(selection) - 1]]

        files_to_import = list(filter(lambda file_to_import: 'model' in file_to_import,
                                      filtered_selection))
        for file_to_import in files_to_import:
            with yaspin(text=("Importing file: %s" % file_to_import['file_name']),
                        color="yellow") as spinner:
                filename = constants.DOWNLOAD_PATH + \
                    file_to_import['file_name']
                dbimport.import_data_to_db(filename, file_to_import['model'])
                spinner.ok("✔")
    else:
        click.echo("❌  - Invalid input")


@main.command()
def shapefiles():
    """
    -- 🗺 Import all shape files to raw
    """
    click.echo("🗺  - Importing raw files to database")
    util.download_file(constants.BALTIMORE_SHAPEFILE_URL,
                       constants.BALTIMORE_SHAPEFILE_LOCATION)
    zip_ref = zipfile.ZipFile(
        constants.DOWNLOAD_PATH + constants.BALTIMORE_SHAPEFILE_LOCATION, 'r')
    zip_ref.extractall(constants.DOWNLOAD_PATH)


@main.command()
def start():
    """
    -- 🎆 Start application locally
    """
    click.echo("🎆  - Starting application")


if __name__ == "__main__":
    main()
