# Script 3

# This script categorizes the countries by continent and shows some descriptive
# statistics about the countries and continents, such as the population and
# population density of each country, which countries are in each continent,
# the number of countries per continent, and the population of each continent.
# I also calculated the total number of countries in the world and the global
# population. Finally, I assigned each country to its quintile based on its number
# of imperiled species. All of these outputs create basic visualizations of the
# conditions in each country.

import pandas as pd
import geopandas as gpd

# These commands make sure that all of the columns and rows are displayed when I print data.
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.options.display.width = 0

# I solely used "map_data.gpkg" from this point forward because it includes
# the exact countries and territories that will be mapped ("all_countries_data.csv"
# was useful to construct the variables that will be used for analyses).
map_data = gpd.read_file("map_data.gpkg")

# I dropped the "geometry" column to reduce the size of map_data so that it's workable
# (otherwise I'd have to wait minutes for it to load because the file's massive).
# However, the geometry column is not lost as it will be used for mapping.
map_data = map_data.drop(columns="geometry")

# In order for the outputs to display properly, I had to shorten the column names.
map_data = map_data.rename(columns={"Population_(in_millions)":"Pop_(millions)","Population_Density":"Pop_Density"})

#%% Before I could analyze continents, I had to create a basic DataFrame that removes extraneous variables.
cc_list = ["Continent","Region","Country_or_Area","Pop_(millions)","Pop_Density"]
cc = map_data[cc_list]

#%% Then I created DataFrames for each continent and calculated descriptive statistics.
africa = cc.query("Continent == 'Africa'")
print("\nCountries and Territories in Africa, with Populations:\n",africa[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("\nTotal Countries and Territories in Africa:",len(africa))
print("\nTotal Population of Africa (in millions):",africa["Pop_(millions)"].sum())

#%% Since the original data lumps North America and South America together as
#   "Americas", I had to separate both continents before I could query them and
#   make calculations.
americas = cc.query("Continent == 'Americas'")
in_americas = americas["Region"] != 'South America'

#%%
n_america = americas[in_americas]
print("\nCountries and Territories in North America, with Populations:\n",n_america[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("\nTotal Countries and Territories in North America:",len(n_america))
print("\nTotal Population of North America (in millions):",n_america["Pop_(millions)"].sum())

#%%
s_america = cc.query("Region == 'South America'")
print("\nCountries and Territories in South America, with Populations:\n",s_america[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("Total Countries and Territories in South America:",len(s_america))
print("\nTotal Population of South America (in millions):",s_america["Pop_(millions)"].sum())

#%%
asia = cc.query("Continent == 'Asia'")
print("\nCountries and Territories in Asia, with Populations:\n",asia[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("\nTotal Countries and Territories in Asia:",len(asia))
print("\nTotal Population of Asia (in millions):",asia["Pop_(millions)"].sum())

#%%
europe = cc.query("Continent == 'Europe'")
print("\nCountries and Territories in Europe, with Populations:\n",europe[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("\nTotal Countries and Territories in Europe:",len(europe))
print("\nTotal Population of Europe (in millions):",europe["Pop_(millions)"].sum())

#%%
oceania = cc.query("Continent == 'Oceania'")
print("\nCountries and Territories in Oceania, with Populations:\n",oceania[["Country_or_Area","Pop_(millions)","Pop_Density"]].sort_values("Pop_(millions)"))
print("\nTotal Countries and Territories in Oceania:",len(oceania))
print("\nTotal Population of Oceania (in millions):",oceania["Pop_(millions)"].sum())

#%% Then I calculate the number of countries in the world and the global population for reference.
total_countries = list(set(cc.index))
print("\nTotal Countries and Territories in the World:",len(total_countries))
print("\nGlobal Population (in millions):\n",cc["Pop_(millions)"].sum())

#%% Here is where I assigned each country to its quintile based on its number
#   of imperiled species.
species_quints = pd.qcut(map_data["Number_of_Imperiled_Species"],5,labels=range(5))
map_data["species_quints"] = species_quints
print("\nCountries by Quintile for Number of Imperiled Species:\n",map_data[["Country_or_Area","species_quints"]].sort_values("Country_or_Area"))

#%% Note that I didn't need to save any output files from this script.