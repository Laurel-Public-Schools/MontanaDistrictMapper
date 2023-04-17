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
all_districts = (primary_schools._append(secondary_schools))._append(unified_districts)

# Plot primary school districts
fig, ax = plt.subplots(figsize=(mapsize_inches_x, mapsize_inches_y))
all_districts.plot(ax=ax,  alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
ax.set_title('Montana School Districts')
ax.set_xlim(all_districts.total_bounds[0], all_districts.total_bounds[2])
ax.set_ylim(all_districts.total_bounds[1], all_districts.total_bounds[3])
ax.set_aspect('equal')
# remove the axis
ax.set_axis_off()

for img in ax.get_images():
    img.set_interpolation('bicubic')

ctx.add_basemap(ax, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik, crs=secondary_schools.crs)
plt.savefig('AllDistricts.png', dpi=imageDPI)
#plt.show()
