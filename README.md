# Mapping.py

This Python script allows you to generate a map file of school districts. The user is prompted to select either elementary or high school districts, or both. They are then asked to input a part of the name of the district they're interested in, and the script searches for matches. Once a match is found, a map file is generated with the district(s) highlighted.

![All Montana Districts](AllDistricts.png?raw=true "All Montana Districts")

## Prerequisites

To use this script, you will need the following Python libraries installed:

- contextily
- geopandas
- matplotlib

## Usage

1. Clone the repository and navigate to the directory where the `Mapping.py` file is located.
2. Edit the `config.py` file to match your configuration preferences (see below).
3. Run the `Mapping.py` file with Python 3. 

## Configuration
In the `config.py` file, you can customize the following parameters:

- `shapefilePrimary`: The path to the shapefile containing the primary school districts.
- `shapefileSecondary`: The path to the shapefile containing the secondary school districts.
- `shapeEdgeColor`: The color of the edges of the district shapes.
- `shapeFaceColor`: The color of the faces of the district shapes.
- `mapZoomLevel`: The level of zoom for the generated map file. Higher numbers have more detail but take longer. Default 15 as the map will then have names for local roads. Set this to 10 to speed up testing.
- `imageDPI`: The resolution of the generated map file.
- `mapsize_inches_x`: The width of the generated map file. Also impacts the resolution of the generated map file.
- `mapsize_inches_y`: The height of the generated map file. Also impacts the resolution of the generated map file.

## Example
Here's an example of how to use the script:

1. Clone the repository and navigate to the directory where the `Mapping.py` file is located.
2. Edit the `config.py` file to match your configuration preferences.
3. Run the `Mapping.py` file with Python 3.
4. When prompted, select `1` for elementary school districts.
5. When prompted, enter `laurel` as the name of the district you're interested in.
6. Wait for the map file to be generated.
7. Open the map file (`output.png`) to view the highlighted district(s).

## Credits
This project uses data from OpenStreetMap. Copyright OpenStreetMap contributors and available under the Open Database License (ODbL)
For more information on this, please view their copyright information here: https://www.openstreetmap.org/copyright

This script was written by Devan Rodabough and is licensed under the MIT License.
