import pandas as pd
import numpy as np 
import os
import json
import geopandas as gpd
import os
import json
from get_data import get_data
import process

def data():
	cfg = json.load(open('ass1.json'))
	get_data(**cfg)
	return

def process():
	pre2018_cleaned = process.pre18(data_test())

def data_test():
	data()
	sub = pd.read_csv('data-test.csv')
	return sub