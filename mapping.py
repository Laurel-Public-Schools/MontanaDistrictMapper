#!/usr/bin/env python3

import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from config import shapefilePrimary, shapefileSecondary, elemDistrictName, secondaryDistrictName, shapeEdgeColor, shapeFaceColor, mapZoomLevel, imageDPI

# read in the first shapefile
shapes = gpd.read_file(shapefilePrimary)
elementaryDistrict = shapes1.loc[shapes1['NAME'] == elemDistrictName]

# read in the second shapefile
shapes2 = gpd.read_file(shapefileSecondary)
highschoolDistrict = shapes2.loc[shapes2['NAME'] == secondaryDistrictName]

# create a plot with a basemap
fig, ax = plt.subplots(figsize=(72, 60))
elementaryDistrict.plot(ax=ax, facecolor=shapeFaceColor, alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
highschoolDistrict.plot(ax=ax, facecolor=shapeFaceColor, alpha=.15, zorder=2, edgecolor=shapeEdgeColor)
ctx.add_basemap(ax, crs=elemDistrictName.crs, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik)

# load the image
img = mpimg.imread('my_map.png')

# plot the image with interpolation
ax.imshow(img, extent=[-109.66, -109.52, 45.88, 45.98], interpolation='bicubic')

# remove the axis
ax.set_axis_off()

# save the figure with a specific DPI
plt.savefig('my_map_with_image.png', dpi=imageDPI)

# show the plot
plt.show()
