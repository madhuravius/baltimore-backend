# -*- coding: utf-8 -*-
"""
Command line utility
"""
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
    """
    click.echo("🤖  - Importing raw files to database")
    filename = constants.DOWNLOAD_PATH + \
        constants.FILE_PARENT_MAPPING[0]['file_name']
    dbimport.import_data_to_db(
        filename, constants.FILE_PARENT_MAPPING[0]['model'])


@main.command()
def start():
    """
    -- 🎆 Start application locally
    """
    click.echo("🎆  - Starting application")


if __name__ == "__main__":
    main()
