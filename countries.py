# Script 1

# In this script, I imported five data files to combine them into a master DataFrame, which
# I used as the starting point for another DataFrame that I later use for all of the analyses
# and mapping.

import pandas as pd

# The following four files are sourced from the UN (data.un.org). I renamed them as follows:
# "UNSD - Methodology.xlsx" to "country_statistics.xlsx"
# URL: https://unstats.un.org/unsd/methodology/m49/overview/
country_data = pd.read_excel("country_statistics.xlsx")

# "SYB64_1_202110_Population, Surface Area and Density.csv" to "global_pops.xlsx"
# URL: https://data.un.org/_Docs/SYB/CSV/SYB64_1_202110_Population,%20Surface%20Area%20and%20Density.csv
country_demos = pd.read_excel("global_pops.xlsx")

#"SYB64_313_202110_Threatened Species.csv" to "threatened_species_by_country.xlsx"
# URL: https://data.un.org/_Docs/SYB/CSV/SYB64_313_202110_Threatened%20Species.csv
species_data = pd.read_excel("threatened_species_by_country.xlsx")

# "SYB64_145_202110_Land.csv" to "country_land_area.xlsx"
# URL: https://data.un.org/_Docs/SYB/CSV/SYB64_145_202110_Land.csv
land_area = pd.read_excel("country_land_area.xlsx")

# This file is from the World Bank (data.worldbank.org). I renamed it from
# "API_AG.LND.AGRI.ZS_DS2_en_csv_v2_3930650.zip" to "income_groups.xlsx"
# URL: https://data.worldbank.org/indicator/AG.LND.AGRI.ZS
income_groups = pd.read_excel("income_groups.xlsx")


#%% Before I did anything in Python, I cleaned all of the files sourced from
#   the United Nations. For each of these files, I manually moved the cell that
#   was originally in B1 to B2, then I manually deleted row 1 in the file.

country_data = country_data.drop(columns=["Global Code","Global Name","Region Code","Sub-region Code","Sub-region Name","Intermediate Region Code","ISO-alpha2 Code","Least Developed Countries (LDC)","Land Locked Developing Countries (LLDC)","Small Island Developing States (SIDS)"])
country_data = country_data.rename(columns={"Region Name":"Continent","Intermediate Region Name":"Region","Country or Area":"Country_or_Area","M49 Code":"Country_Number","ISO-alpha3 Code":"Country_Code"})

# Note that the population and species data are for 2021. Also, I don't know what
# units population density is measured by, so I'm just using the numbers as they
# appear in the original file.
country_demos = country_demos.drop(columns=["Footnotes","Source"])
country_demos = country_demos.rename(columns={"Region/Country/Area":"Country_Number","Population, density and surface area":"Country_or_Area","Year":"Year_(pop)"})
set1 = country_demos.query("`Year_(pop)` == 2021")
set1 = set1.query("Series == 'Population mid-year estimates (millions)'")
set1 = set1.drop(columns="Series")
set1 = set1.rename(columns={"Value":"Population_(in_millions)"})
set2 = country_demos.query("`Year_(pop)` == 2021")
set2 = set2.query("Series == 'Population density'")
set2 = set2.drop(columns="Series")
set2 = set2.rename(columns={"Value":"Population_Density"})
sets = pd.merge(set1,set2,on="Country_Number")
sets = sets.rename(columns={"Country_or_Area_x":"Country_or_Area","Year_(pop)_x":"Year_(pop)"})
country_demos = sets.drop(columns=["Country_or_Area_y","Year_(pop)_y"])

species_data = species_data.drop(columns=["Footnotes","Source"])
species_data = species_data.rename(columns={"Region/Country/Area":"Country_Number","Threatened species":"Country_or_Area","Value":"Number_of_Imperiled_Species","Series":"Measurement"})
species_data = species_data.query("Year == 2021")
species_data = species_data.query("Measurement == 'Threatened Species: Vertebrates (number)'")

land_area = land_area.drop(columns=["Footnotes","Source"])
land_area = land_area.rename(columns={"Region/Country/Area":"Country_Number","Land":"Country_or_Area","Value":"Land_Area_(thousand_hectares)","Series":"Measurement"})
land_area = land_area.query("Measurement == 'Land area (thousand hectares)'")
land_area = land_area.query("Year == 2018")
land_area = land_area.drop(columns=["Year","Measurement"])

# Then I cleaned the World Bank file.
income_groups = income_groups.drop(columns=["Region","SpecialNotes"])
income_groups = income_groups.rename(columns={"Country Code":"Country_Code","IncomeGroup":"Income_Group","TableName":"Country_or_Area"})

#%% After all of the data has been imported and cleaned, I merged each of DataFrames
# to create a master DataFrame ("merge_countries").
merge1 = pd.merge(country_data,country_demos,on="Country_Number")
merge1 = merge1.rename(columns={"Country_or_Area_x":"Country_or_Area"})
merge1 = merge1.drop(columns="Country_or_Area_y")
merge2 = pd.merge(merge1,land_area,on="Country_Number")
merge2 = merge2.rename(columns={"Country_or_Area_x":"Country_or_Area"})
merge2 = merge2.drop(columns="Country_or_Area_y")
merge3 = pd.merge(merge2,income_groups,on="Country_Code")
merge_countries = pd.merge(merge3,species_data,on="Country_Number")
merge_countries = merge_countries.drop(columns=["Country_or_Area_x","Year_(pop)","Country_or_Area_y"])
merge_countries = merge_countries.drop(columns=["Year","Measurement"])
merge_countries.set_index("Country_or_Area",inplace=True)
merge_countries = merge_countries.sort_values("Country_or_Area")

#%% Finally, I saved the master DataFrame as a CSV file so that I could use it in subsequent scripts.
merge_countries.to_csv("all_countries_data.csv")