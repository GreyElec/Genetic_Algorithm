import numpy as np
import pandas as pd

import re
data = []
#with open("C:\\Users\\Silver\\Desktop\\ATM_CITY_input_raw_small.txt") as f:
#	for each in f:
#		data.append(each.split('~')[:-1])
#with open("C:\\Users\\Silver\\Desktop\\ATM_CITY_input_raw.txt") as f2:
map_List = []
with open("C:\\Users\\Silver\\Desktop\\worldcitiespop.csv") as map:
		map_List = [next(map).split(',') for i in range(100)]
with open("C:\\Users\\Silver\\Desktop\\ATM_CITY_input_raw.txt") as fd:
	for each in f:
		data.append(each.split('~'))
data_Frame = pd.DataFrame(data)

print(data_Frame[0:5])
map_Frame = pd.DataFrame(map_List)
#print(map_Frame)
map_Frame.drop(2,axis=1,inplace=True)
print(map_Frame)
#print(data[:-1])
#data = data[:-1]
#for i in range(len(data)):
##		data[i][j] = data[i][j].lower()
#		data[i][j] = data[i][j].strip()
#print(data)
#data_Frame = pd.DataFrame(data)
#print(data_Frame)
#print(map_Frame[1:5])
#map_Frame = map_Frame.drop("AccentCity",axis=0,inplace=True)
#print(map_Frame[:5])