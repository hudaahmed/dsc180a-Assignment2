
import os
import pandas as pd
import json
import glob
import numpy as np
import doctest
import datetime as dt
import geopandas as gpd


def get_data(years, components, outpath):
    web = 'http://seshat.datasd.org/pd/vehicle_stops_'
    for year in years:
        if year < 2018:
            url = web + str(year) + '_datasd_v1.csv'
            tables = pd.read_csv(url)
            if not os.path.exists(outpath):
                os.mkdir(outpath)
            tables.to_csv("%s/%s.csv"%(outpath, year))
        else:
            url = 'http://seshat.datasd.org/pd/ripa_stops_datasd_v1.csv'
            tables = pd.read_csv(url)
            if not os.path.exists(outpath):
                os.mkdir(outpath)
            tables.to_csv("%s/%s.csv"%(outpath, year))
            
    for comps in components:
        url = 'http://seshat.datasd.org/pd/ripa_' + comps + '_datasd.csv'
        tables = pd.read_csv(url)
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        tables.to_csv("%s/%s.csv"%(outpath, comps))
        
        
def make_df(years, components, outpath): 
    df = pd.DataFrame()
    for i in years:
        if i < 2018:
            path = 'assn1/' + str(i) + '.csv'
            table = pd.read_csv(path)
        else:
            continue
        newtab = pd.concat([df, table], axis = 0).reset_index(drop=True)
    return newtab


def binary_clean(ser):
    sez = []
    for i in range(len(ser)):
        if type(ser[i]) == float:
            sez.append(0)
        elif ser[i] == 'Y' or ser[i] == 'y':
            sez.append(1)
        else:
            sez.append(0)
    return sez

def clean_age(ser):
    sez = []
    for i in range(len(ser)):
        if type(ser[i])== float:
            sez.append(0)
        elif ser[i] == 'M':
            sez.append(1)
        elif ser[i] == 'F':
            sez.append(2)
        else:
            sez.append(3)
    return sez

def clean_post(ser):
    sez = []
    for i in range(len(ser)):
        if type(ser[i])== float:
            sez.append(0)
        else:
            sez.append(1)
    return sez

races = {'A':'Middle Eastern or South Asian',
'B':'Black/African American',
'C':'Asian',
'D':'Asian',
'F':'Asian',
'G':'Pacific Islander',
'H':'Hispanic/Latino/a',
'I':'Middle Eastern or South Asian',
'J':'Asian',
'K':'Asian',
'L':'Asian',
'O':'Other',
'P':'Pacific Islander',
'S':'Pacific Islander',
'U':'Pacific Islander',
'V':'Asian',
'W':'White',
'Z':'Middle Eastern or South Asian'}

wanted_columns_pre = ['stop_id', 'stop_cause', 'date_stop', 'time_stop', 'subject_race', 'subject_sex', 'subject_age', 'service_area', 'sd_resident', 'property_seized', 'searched']
wanted_columns_post = ['stop_id', 'reason_for_stop', 'date_stop', 'time_stop', 'race', 'gend', 'perceived_age', 'beat', 'address_city', 'type_of_property_seized', 'basis_for_search']



