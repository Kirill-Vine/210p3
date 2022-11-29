import math
import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
from numpy import nan as NA
import csv  
f = open("EuCitiesTemperatures.csv")
data = pd.read_csv(f)
lst=Series(list(data['latitude']), index=data['country'].values)
newlatlist=[]
for i in data.index:
    if math.isnan(data['latitude'][i]):
        newlatlist.append(round(np.nanmean(np.array(lst[data['country'][i]])),2))
    else:
        newlatlist.append(data['latitude'][i])
data['latitude']=newlatlist
lst1=Series(list(data['longitude']), index=data['country'].values)
newlonglist=[]
for i in data.index:
    if math.isnan(data['longitude'][i]):
        newlonglist.append(round(np.nanmean(np.array(lst1[data['country'][i]])),2))
    else:
        newlonglist.append(data['longitude'][i])
data['longitude']=newlonglist
data.to_csv("EuCitiesTemperatures.csv", columns=data.columns)
