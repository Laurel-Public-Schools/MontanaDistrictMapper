#!/usr/bin/env python3

import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from config import shapefilePrimary, shapefileSecondary, elemDistrictName, secondaryDistrictName, shapeEdgeColor, shapeFaceColor, mapZoomLevel, imageDPI

# read in the first shapefile
if elemDistrictName is not None:
    shapes1 = gpd.read_file(shapefilePrimary)
    elementaryDistrict = shapes1.loc[shapes1['NAME'] == elemDistrictName]

# read in the second shapefile
if secondaryDistrictName is not None:
    shapes2 = gpd.read_file(shapefileSecondary)
    highschoolDistrict = shapes2.loc[shapes2['NAME'] == secondaryDistrictName]

# create a plot with a basemap
fig, ax = plt.subplots(figsize=(72, 60))
elementaryDistrict.plot(ax=ax, facecolor=shapeFaceColor, alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
highschoolDistrict.plot(ax=ax, facecolor=shapeFaceColor, alpha=.15, zorder=2, edgecolor=shapeEdgeColor)
ctx.add_basemap(ax, crs=elementaryDistrict.crs, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik)

# apply interpolation to the basemap image
for img in ax.get_images():
    img.set_interpolation('bicubic')


# remove the axis
ax.set_axis_off()

# save the figure with a specific DPI
plt.savefig('my_map_with_image.png', dpi=imageDPI)

# show the plot
plt.show()