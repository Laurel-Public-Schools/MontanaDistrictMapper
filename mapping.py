#!/usr/bin/env python3

import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from config import shapefilePrimary, shapefileSecondary, shapefileUnified, shapeEdgeColor, shapeFaceColor, mapZoomLevel, imageDPI, mapsize_inches_x, mapsize_inches_y

elemDistrictName = None
secondaryDistrictName = None
unifiedDistrictName = None
shapes = None

while shapes is None:
    print("Please select from one of the following options:")
    print("For an Elementary District input 1")
    print("for a High School District input 2")
    print("for both types of Districts input 3")
    print("for Unified Districts input 4")
    district_type = input()
    print("You have input " + district_type + ".")
    if district_type == "1":
        shapes = gpd.read_file(shapefilePrimary)
    elif district_type == "2":
        shapes = gpd.read_file(shapefileSecondary)
    elif district_type == "3":
        shapes = gpd.read_file(shapefilePrimary)
        secondary_shapes = gpd.read_file(shapefileSecondary)
    elif district_type =="4":
        shapes = gpd.read_file(shapefileUnified)
    else:
        print("That was not a valid answer. Please try again.")
 

matches = gpd.GeoDataFrame()  
while matches.empty and district_type != '3':
    print("Please type in a part of your school's name:")
    selected_district = input()
    print("You have input " + selected_district + ".")
    matches = shapes.loc[shapes["NAME"].str.contains(selected_district, case=False)]
    if matches.empty:
        print("It seems we did not locate a school that contains " + selected_district + ".")
        print("Please Try again.")
    elif matches.count()[0] >= 2:
        print("There were multiple matches.")
        print("Here they are:")
        print(matches["NAME"].to_string(index=False))
        selected_district = input("Please enter the exact name of the district you are looking for: ")
        matches = matches.loc[matches["NAME"].str.contains(selected_district, case=False)]
        if matches.empty:
            print("Could not find a district with that name. Please try again.")
    
if district_type == '1':
    elemDistrictName = matches
elif district_type == '2':
    secondaryDistrictName = matches
elif district_type == '4':
    unifiedDistrictName = matches
    
## for option 3 ##
while matches.empty and district_type == "3":
    print("Please type in a part of your Elementary District's Name")
    selected_district = input()
    print("You have input " + selected_district + ".")
    matches = shapes.loc[shapes["NAME"].str.contains(selected_district, case=False)]
    if matches.empty:
        print("It seems we did not locate a school that contains " + selected_district + ".")
        print("Please Try again.")
    elif matches.count()[0] >= 2:
        print("There were multiple matches.")
        print("Here they are:")
        print(matches["NAME"].to_string(index=False))
        selected_district = input("Please enter the exact name of the district you are looking for: ")
        matches = matches.loc[matches["NAME"].str.contains(selected_district, case=False)]
        if matches.empty:
            print("Could not find a district with that name. Please try again.")
    elemDistrictName = matches
    print("We found the match " + elemDistrictName["NAME"].to_string(index=False) + ".")
    #This holds on to Elementary Matches and we can just redo the code##
    print("Please type in a part of your High School District's Name")
    selected_district = input()
    print("You have input " + selected_district + ".")
    matches = secondary_shapes.loc[secondary_shapes["NAME"].str.contains(selected_district, case=False)]
    if matches.empty:
        print("It seems we did not locate a school that contains " + selected_district + ".")
        print("Please Try again.")
    elif matches.count()[0] >= 2:
        print("There were multiple matches.")
        print("Here they are:")
        print(matches["NAME"].to_string(index=False))
        selected_district = input("Please enter the exact name of the district you are looking for: ")
        matches = matches.loc[matches["NAME"].str.contains(selected_district, case=False)]
        if matches.empty:
            print("Could not find a district with that name. Please try again.")
    secondaryDistrictName = matches
    matches = matches._append(elemDistrictName)
    print("The elementary district is " + elemDistrictName["NAME"].to_string(index=False))
    print("The High School district is " + secondaryDistrictName["NAME"].to_string(index=False))



print("These are the district names that have like values:")
print(matches["NAME"].to_string(index=False))
print("Generating the map file!")
print("This may take some time...")

#####
fig, ax = plt.subplots(figsize=(mapsize_inches_x, mapsize_inches_y))
if elemDistrictName is not None:
    elemDistrictName.plot(ax=ax, facecolor=shapeFaceColor, alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
    ctx.add_basemap(ax, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik, crs=elemDistrictName.crs)

if secondaryDistrictName is not None:
    secondaryDistrictName.plot(ax=ax, facecolor=shapeFaceColor, alpha=.15, zorder=2, edgecolor=shapeEdgeColor)
    if elemDistrictName is None:
        ctx.add_basemap(ax, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik, crs=secondaryDistrictName.crs)

if unifiedDistrictName is not None:
    unifiedDistrictName.plot(ax=ax, facecolor=shapeFaceColor, alpha=.25, zorder=1, edgecolor=shapeEdgeColor)
    ctx.add_basemap(ax, zoom=mapZoomLevel, source=ctx.providers.OpenStreetMap.Mapnik, crs=unifiedDistrictName.crs)

# apply interpolation to the basemap image
for img in ax.get_images():
    img.set_interpolation('bicubic')


# remove the axis
ax.set_axis_off()

# save the figure with a specific DPI
plt.savefig('output.png', dpi=imageDPI)

# show the plot
plt.show()