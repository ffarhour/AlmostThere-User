"""

.. module: Mapping Bus Route Shapes
.. moduleauthor: Farmehr Farhour f.farhour@gmail.com

"""
#import requests
import requests
#import json
import json

#query the api server
url = requests.get("http://api.at.govt.nz/v1/gtfs/shapes/tripId/0070ML577521154231898?api_key=0dd6fe7c-5b44-45db-a5c2-023558a490d3")
#convert to python 
data = url.json()
#store the response only
if data['status']=='OK':
    response = data['response']
else:
    print('ERROR')

#define lat/long lists
latlist = []
longlist = []

#loop through the list of dictionaries & store lat/long points in appropriate lists
for a in response:
    latlist.append(a['shape_pt_lat'])
    longlist.append(a['shape_pt_lon'])




from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='merc',llcrnrlat=-37,urcrnrlat=-36.6144,\
            llcrnrlon=174.6442,urcrnrlon=174.9188,lat_ts=20,resolution='h')
#m.drawcoastlines()
#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawcountries()

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')

#read all shape files
import os
for file in os.listdir("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/"):
    if file.endswith("reprojected.shp"):
        filename = file.split(".")[0]
        path = "C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/"
        m.readshapefile(path + filename,filename)

"""
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/road_cl_reprojected",'roads')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/building_poly_reprojected",'building_poly')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/coastline_reprojected",'coastline')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/island_poly_reprojected",'island_poly')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/lake_poly_reprojected",'lake_poly')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/residential_area_poly_reprojected",'residential_area_poly')
m.readshapefile("C:/Users/F.Farhour/Downloads/Maps/BA32_Shapev1-03/BA32/breakwater_cl_reprojected",'breakwater_cl')
"""


#put a point on the map
"""
#location of 2 points
lon = [174.70428,174.9,]

lat = [-36.75, -36.852671]
"""
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
xpt,ypt = m(longlist,latlist)

"""
# convert back to lat/lon
lonpt, latpt = m(xpt,ypt,inverse=True)
"""
m.plot(xpt,ypt,'bo')  # plot a blue dot there


'''
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
plt.text(xpt+100000,ypt+100000,'Some point (%5.1fE,%3.1fS)' % (lonpt,latpt))
'''

plt.title("Mercator Projection - Auckland")
plt.show()

