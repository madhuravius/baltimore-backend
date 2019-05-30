# -*- coding: utf-8 -*-
"""
Utility files to facilitate/automate database imports
"""
import csv


def import_data_to_db(filename, model):  # , mapping, model):x
    '''
    Example where filename = './raw/Police_use_of_force_and_in-custody_injuries.csv'
    Example where model is
    importDataToDB(filename, model)
    '''
    with open(filename, 'r') as file_to_open:
        reader = csv.reader(file_to_open, delimiter=',')
        count = 0
        for line in reader:
            count += 1
            if count > 1:  # skip first line (field labels/names)
                model.insert_from_csv(None, line)
