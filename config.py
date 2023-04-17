import os
import urllib.request
import zipfile

# URL and filename for the zipped file
file_web_location = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/AdministrativeBoundaries/MontanaSchoolDistricts_shp.zip'
filename = 'MontanaSchoolDistricts_shp.zip'

# Shapefile path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is root of github project
SHAPEFILES_DIR = os.path.join(ROOT_DIR, 'MontanaSchoolDistricts_shp')
shapefilePrimary = os.path.join(SHAPEFILES_DIR, 'Elementary.shp')
shapefileSecondary = os.path.join(SHAPEFILES_DIR, 'Secondary.shp')
shapefileUnified = os.path.join(SHAPEFILES_DIR, 'Unified.shp')
# Download the zipped file from the web
urllib.request.urlretrieve(file_web_location, filename)

# Extract the zipped file to the correct directory
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(ROOT_DIR)

# Remove the downloaded zip file
os.remove(filename)

# Set Map Properties #
shapeEdgeColor = 'black'
shapeFaceColor = 'gold'
mapZoomLevel = 15
imageDPI = 600
mapsize_inches_x = 60
mapsize_inches_y = 72
