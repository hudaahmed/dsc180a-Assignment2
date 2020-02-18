import pandas as pd
import os
import json
import glob
import numpy as np
import doctest
import datetime as dt
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoSeries
from shapely.geometry import Polygon
import sys


from process import *
from data import *

cfg = json.load(open('ass1.json'))
get_data(**cfg)
df1 = make_df(**cfg)
owd = os.getcwd()
os.chdir("assn1")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
all_filenames = np.sort(all_filenames)
newnames = all_filenames[:4]
pre2018 = pd.concat([pd.read_csv(f) for f in newnames ]).reset_index(drop = True)
pre2018 = pre2018[wanted_columns_pre]

stops = pd.read_csv(all_filenames[-1])
newstops = stops[['stop_id', 'reason_for_stop']]
searched = pd.read_csv(all_filenames[-2])
searched2 = searched[['stop_id', 'basis_for_search']]

post2018 = pd.read_csv(all_filenames[4])
post2018 = post2018.merge(pd.read_csv(all_filenames[5]), on='stop_id')
post2018 = post2018.drop_duplicates(subset = 'stop_id')
post2018 = post2018.merge(pd.read_csv(all_filenames[6]), on='stop_id')
post2018 = post2018.drop_duplicates(subset = 'stop_id')
post2018 = post2018.merge(newstops, on='stop_id')
post2018 = post2018.drop_duplicates(subset = 'stop_id')
post2018 = post2018.merge(searched2, on='stop_id' )
post2018 = post2018.drop_duplicates(subset = 'stop_id')
post2018 = post2018[wanted_columns_post]

pre2018 = pre18(pr2018)
post2018 = post18(pt2018)

allyears = pd.concat([pre2018, post2018], axis = 0).reset_index(drop=True)

i = ((allyears['time_stop'] >= '17:09:00') & (allyears['time_stop'] <= '20:29:00'))
z = allyears.loc[i]
len(z)/len(allyears)