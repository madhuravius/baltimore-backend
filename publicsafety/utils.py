"""
Public safety utils
"""
# -*- coding: utf-8 -*-

from datetime import datetime

def get_start_date_end_date_params(request):
    """
    cleans start/end dates parameters for use or simply omits them
    """
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%m-%d-%Y')
        end_date = datetime.strptime(end_date, '%m-%d-%Y')
        return start_date, end_date
    return False, False


def get_map_locations(request):
    """
    cleans boolean filter parameter (for map locaitons) and only allows locations with lat/longs
    """
    return request.query_params.get('get_map_locations', False)
