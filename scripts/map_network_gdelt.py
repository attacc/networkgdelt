import pandas as pd
import sqlite3
import datetime as dt
from collections import defaultdict
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sys

con = sqlite3.connect("test.db")

q = """
SELECT
ActionGeo_Lat,ActionGeo_Long
FROM
gdelt
WHERE
Actor1CountryCode == 'SYR'
AND
Actor2CountryCode == 'SYR';
"""

#gdelt.to_sql("gdelt",con,if_exists="replace")

syr_data=pd.read_sql_query(q,con)

# Note that we're drawing on a regular matplotlib figure, so we set the 
# figure size just like we would any other.
plt.figure(figsize=(12,12))

# Create the Basemap
event_map = Basemap(projection='merc', 
                    resolution='l', area_thresh=1000.0, # Low resolution
                    lat_0 = 55.0, lon_0=60.0, # Map center 
                    llcrnrlon=10, llcrnrlat=20, # Lower left corner
                    urcrnrlon=100, urcrnrlat=70) # Upper right corner

# Draw important features
event_map.drawcoastlines() 
event_map.drawcountries()
event_map.fillcontinents(color='0.8') # Light gray
event_map.drawmapboundary()

# Draw the points on the map:
for row in syr_data.iterrows():
    x, y = event_map(row[1][0], row[1][1] ) # Convert lat, long to y,x
    marker_size = 20.0
    event_map.plot(x,y, 'ro', markersize=marker_size, alpha=0.3)

plt.show()



