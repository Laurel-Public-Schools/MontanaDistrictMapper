import os
import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
from config import shapefilePrimary, shapefileSecondary, shapefileUnified, shapeEdgeColor

imageDPI = 300

# Set Map Properties #
mapZoomLevel = 8
mapsize_inches_x = 30
mapsize_inches_y = 30

# Read shapefiles
primary_schools = gpd.read_file(shapefilePrimary)
secondary_schools = gpd.read_file(shapefileSecondary)
unified_districts = gpd.read_file(shapefileUnified)
all_districts = primary_schools._append(secondary_schools).append(shapefileUnified)

# Plot primary school districts
fig, ax = plt.subplots(figsize=(mapsize_inches_x, mapsize_inches_y))
all_districts.plot(ax=ax,  alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
ax.set_title('Montana Primary School Districts')
ax.set_xlim(all_districts.total_bounds[0], all_districts.total_bounds[2])
ax.set_ylim(all_districts.total_bounds[1], all_districts.total_bounds[3])
ax.set_aspect('equal')

ctx.add_basemap(ax, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik, crs=secondary_schools.crs)
plt.show()
plt.savefig('AllDistricts.png', dpi=imageDPI)
