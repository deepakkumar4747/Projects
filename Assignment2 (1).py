
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
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

# In[2]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[4]:

import numpy as np
df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df=df.sort('Date')[df['Date']<='2014-12-31']

df_Tmax=df[df['Element']=='TMAX']
df_Tmin=df[df['Element']=='TMIN']
df_Tmax=df_Tmax.groupby('Date').agg({'Data_Value':max})
df_Tmin=df_Tmin.groupby('Date').agg({'Data_Value':min})


# In[45]:

df_Tmin.index = pd.to_datetime(df_Tmin.index)
df_Tmax.index = pd.to_datetime(df_Tmax.index)
df_Tmin = df_Tmin[~((df_Tmin.index.month == 2) &(df_Tmin.index.day ==29))]
df_Tmax = df_Tmax[~((df_Tmax.index.month == 2) &(df_Tmax.index.day ==29))]


df2=pd.read_csv('data/C2A2_data/BinnedCsvs_d400/6bfe451be8ad7abced396241683a69ba88103e019d15e945a56d0d05.csv')

df2= df2[df2['Date']>='2015-01-01'].sort('Date')
max_2015 = df2[(df2['Element'] == 'TMAX')].groupby('Date').aggregate({'Data_Value':np.max})
min_2015 = df2[(df2['Element'] == 'TMIN')].groupby('Date').aggregate({'Data_Value':np.min})
min_2015.index = pd.to_datetime(min_2015.index)
max_2015.index = pd.to_datetime(max_2015.index)

Iloc_broken_max = np.where(max_2015['Data_Value'] > df_Tmax['Data_Value'].max())
Iloc_broken_min = np.where(min_2015['Data_Value'] < df_Tmin['Data_Value'].min())


# 

# In[52]:

plt.figure()
plt.plot(df_Tmax.values, label='Max Temp (2005-2014)', linewidth=1, alpha=0.7, color = 'red')
plt.plot(df_Tmin.values, label='Min Temp (2005-2014)', linewidth=1, alpha=0.7, color = 'royalblue')
plt.gca().fill_between(range(len(df_Tmax)), df_Tmin['Data_Value'],df_Tmax['Data_Value'],facecolor='gainsboro',alpha=0.7)
plt.scatter(Iloc_broken_max,max_2015.iloc[Iloc_broken_max], s=10, color='red', label='High Temp Broken(2015)')
plt.scatter(Iloc_broken_min,min_2015.iloc[Iloc_broken_max], s=10, color='royalblue', label='Low Temp Broken(2015)')

plt.legend(loc='best',title='Temperature',fontsize=8)
plt.xticks(np.linspace(0, 30*12, num=12), (r'Jan', r'Feb', r'Mar', r'Apr', r'May', r'Jun', r'Jul', r'Aug', r'Sep', r'Oct', r'Nov', r'Dec'))
plt.yticks(alpha = 0.8)
plt.xlim(0,365)
plt.xlabel('Month')
plt.ylabel('Temperature ($^\\circ$C)')
plt.title('Assignment 2: The interval of minimum and maximum temperatures for 2005-2014 \\n and broken temperatures in 2015 near Ann Arbor, Michigan, United States')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_alpha(0.3)
plt.gca().spines['left'].set_alpha(0.3)
plt.show()


# In[44]:




# In[ ]:




# In[ ]:



