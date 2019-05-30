# -*- coding: utf-8 -*-
"""
Set of utility functions and methods across the django project
"""
import time
import urllib.request

from util import constants


def dl_progress(count, block_size, _):
    """
    Download progress utility function. Shows # of MB downloaded as a string
    """
    print(str(count*block_size/(1024 * 1024)) +
          'MB downloaded', end='\r')


def download_all_raw_data():
    """
    Utility function to download all files set in constants
    """
    for raw_data_mapping in constants.FILE_PARENT_MAPPING:
        timer_start = time.time()
        print("Downloading file: ", raw_data_mapping['file_name'])
        urllib.request.urlretrieve(raw_data_mapping['url'],
                                   constants.DOWNLOAD_PATH +
                                   raw_data_mapping['file_name'],
                                   reporthook=dl_progress)
        timer_end = time.time()
        print("Time to complete download: ", timer_end-timer_start, " seconds")


def download_file(url, filepath):
    """
    Utility function to download url and save to path
    """
    timer_start = time.time()
    print("Downloading file: ", url)
    urllib.request.urlretrieve(url,
                               constants.DOWNLOAD_PATH +
                               filepath,
                               reporthook=dl_progress)
    timer_end = time.time()
    print("Time to complete download: ", timer_end-timer_start, " seconds")
