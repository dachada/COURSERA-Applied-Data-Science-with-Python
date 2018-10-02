
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[45]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[168]:

#Split csv by before 2015 / 2015
dfttl = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv').sort_values('Date').rename(columns={'Date':'Dates'})                    
dfttl = pd.merge(dfttl, dfttl['Dates'].str.split('-', n=1,expand=True).rename(columns={0:'Year',1:'Dt'}), how = 'inner', left_index=True, right_index=True)
dfttl = dfttl[dfttl['Dt']!='02-29']
df2015 = dfttl[dfttl['Year']=='2015']
df = dfttl[dfttl['Year']!='2015']

#Calculate max temp and min temp in each day, over 2005-2014
piv = df.pivot_table(values='Data_Value', index='Dt', columns='Element', aggfunc=[np.max, np.min]).reset_index().drop([('amax', 'TMIN'),('amin','TMAX')],axis=1)
piv2015 = df2015.pivot_table(values='Data_Value', index='Dt', columns='Element', aggfunc=[np.max, np.min]).reset_index().drop([('amax', 'TMIN'),('amin','TMAX')],axis=1)
#Get broken temps in 2015 when comparing to 2005-2014
broken_max = piv2015[(piv['amax'] < piv2015['amax'])].dropna(how='all').drop(['Dt',('amin','TMIN')], axis=1)
broken_min = piv2015[(piv['amin'] > piv2015['amin'])].dropna(how='all').drop(['Dt',('amax','TMAX')], axis=1)

#Create the chart
plt.figure()
plt.gcf().set_size_inches(30,10,forward=True)
#fig, ax = plt.subplots(1,1)
plt.plot(piv[('amax','TMAX')], '-k', piv[('amin','TMIN')], '-k', linewidth=0, alpha=0.7, label='')
plt.gca().fill_between(range(len(piv)),piv[('amax','TMAX')],piv[('amin','TMIN')],facecolor='lightslategrey', alpha=0.3 )
plt.scatter(broken_max.index, broken_max, c ='red', s = 100, label='2015 Broken temp(Max)')
plt.scatter(broken_min.index, broken_min, c ='blue', s = 100, label='2015 Broken temp(Min)')

#Add legend and delete frames 
from matplotlib.ticker import  MultipleLocator
plt.legend(frameon=False,title=False)

#set spines into the middle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 177))

#show x-ticks by bi-week
x_ticks = list(range(0, len(piv.index),15))
x_ticks.append(len(piv.index)-1)
x_labels = [piv['Dt'][i] for i in x_ticks]
plt.xticks(x_ticks)

#Beautify x axis
for i in range(-300, 500, 100):
    if i==0:
        plt.gca().text(170, i, str(i), color='white')
    else:
        plt.gca().text(170, i, str(int(i/10))+'℃', color='black')

plt.title('10-Year Temperature Record Broken Days in 2015\nNear Ann Arbor, Michigan, United States',loc='left',fontdict={'fontsize':'x-large'})
plt.gca().set_xticklabels(x_labels, rotation=90)
plt.tick_params(labelleft=False, labelcolor='black',colors='grey')
plt.margins(0,0)
#plt.grid()

plt.show()





# In[ ]:



