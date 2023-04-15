import os

# Name of Districts according to data on the files
#elemDistrictName = 'ELDER GROVE ELEMENTARY'
#secondaryDistrictName = None
# Shapefile path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is root of github project
SHAPEFILES_DIR = os.path.join(ROOT_DIR, 'MontanaSchoolDistricts_shp')
shapefilePrimary = os.path.join(SHAPEFILES_DIR, 'Elementary.shp')
shapefileSecondary = os.path.join(SHAPEFILES_DIR, 'secondary', 'Secondary.shp')


# Set Map Properties #
shapeEdgeColor = 'black'
shapeFaceColor = 'gold'
mapZoomLevel = 10
imageDPI = 300