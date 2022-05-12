# Script 2

# This script merges the master DataFrame I created in countries.py (merge_countries)
# with a shapefile, which has country coordinates for mapping. The merge produces a
# new master DataFrame (map_data) that combines all of the variables with geographic data,
# so I use it for all of the analyses and mapping.

import pandas as pd
import geopandas as gpd

# First, reimport the CSV file that I created in countries.py.
merge_countries = pd.read_csv("all_countries_data.csv")

#%% Now import the shapefile, sourced from IPUMS International, to create a GeoDataFrame.
# URL: https://international.ipums.org/international/gis.shtml ("World map" file)

world_map = gpd.read_file("IPUMSI_world_release2020.zip")
world_map = world_map.drop(columns=["OBJECTID","BPL_CODE"])
world_map = world_map.rename(columns={"CNTRY_NAME":"Country_or_Area","CNTRY_CODE":"Country_Number"})
world_map.set_index("Country_or_Area",inplace=True)
world_map["Country_Number"] = world_map["Country_Number"].astype(int)

#%% Merge the two DataFrames together to create the new master GeoDataFrame.
map_data = world_map.merge(merge_countries,on="Country_Number")

#%% For mapping, I needed to create columns for species by country land area,
# species by country population, and species by country income group.
map_data["species/area"] = map_data["Number_of_Imperiled_Species"]/map_data["Land_Area_(thousand_hectares)"]

map_data["species/pop"] = map_data["Number_of_Imperiled_Species"]/map_data["Population_(in_millions)"]

grouped = map_data.groupby("Income_Group")
mean_by_income = grouped["Number_of_Imperiled_Species"].mean()

#%% Save map_data as a GeoPackage file for use in subsequent scripts and QGIS.
map_data.to_file("map_data.gpkg",layer="Country_Data",index=False)