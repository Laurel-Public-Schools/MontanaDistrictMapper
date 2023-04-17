#!/usr/bin/env python3

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config import shapefilePrimary, shapefileSecondary


shapes = None

while shapes is None:
    print("Please select from one of the following options:")
    print("For an Elementary District input 1")
    print("for a High School District input 2")
    print("for both types of Districts input 3")
    district_type = input()
    print("You have input " + district_type + ".")
    if district_type == "1":
        shapes = gpd.read_file(shapefilePrimary)
    elif district_type == "2":
        shapes = gpd.read_file(shapefileSecondary)
    elif district_type == "3":
        shapes = gpd.read_file(shapefilePrimary)
        secondary_shapes = gpd.read_file(shapefileSecondary)
    else:
        print("That was not a valid answer. Please try again.")




matches = gpd.GeoDataFrame()  
while matches.empty and district_type is not "3":
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
        matches = matches.loc[matches["NAME"] == selected_district.upper()]
        if matches.empty:
            print("Could not find a district with that name. Please try again.")
## for option 3 ##
while matches.empty and district_type is "3":
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
    print("We found the match " + elementaryMatch["NAME"].to_string(index=False) + ".")
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


print("These are the district names that have like values:")
print(matches["NAME"].to_string(index=False))
print("The elementary district is " + elemDistrictName["NAME"].to_string(index=False))
print("The High School district is " + secondaryDistrictName["NAME"].to_string(index=False))