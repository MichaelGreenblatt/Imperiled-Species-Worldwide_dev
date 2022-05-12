# Script 4

# This final script couples variables together in the following way to graph
# potential relationships:
# -number of imperiled species by country population
# -number of imperiled species by country land area
# -number of imperiled species by country income group
# Each of these comparisons is graphed worldwide, then by the 10 countries that
# have the most imperiled species and the 10 countries that have the fewest imperiled
# species. There are five graphs per comparison because I made graphs displayed
# by continent and by country. All of the graphs follow the same pattern.

# Note: Unfortunately, I couldn't get any of the graphs to save to a file.
# Also, in order for the graphs to load properly, they each have to be run
# individually (line-by-line).

import pandas as pd
import geopandas as gpd
import seaborn as sns

# Once again, I solely used "map_data.gpkg" for the analyses.
map_data = gpd.read_file("map_data.gpkg")
map_data = map_data.drop(columns="geometry")

#%% I needed to relabel the income groups so that they could be sorted properly
#   in the graphs (note that they're only sorted right in fig11 because I
#   couldn't get it to work in fig12, fig13, fig14, or fig15).
short_names = {"Low income":"1 Low","Lower middle income":"2 Lower mid","Upper middle income":"3 Upper mid","High income":"4 High"}
map_data["Income_Group"] = map_data["Income_Group"].replace(short_names)

#%% I also needed to isolate the 10 countries with the most and the 10 countries
#   with the fewest imperiled species.
top_10 = map_data.nlargest(10,['Number_of_Imperiled_Species']).reset_index()
top_10 = top_10.drop(columns="index")
print("10 Countries with the Most Imperiled Species:\n",top_10[["Country_or_Area","Number_of_Imperiled_Species"]])

bottom_10 = map_data.nsmallest(10,["Number_of_Imperiled_Species"]).reset_index()
bottom_10 = bottom_10.drop(columns="index")
print("10 Countries with the Fewest Imperiled Species:\n",bottom_10[["Country_or_Area","Number_of_Imperiled_Species"]])

#%% This graph plots the number of species by country population (worldwide).
fig1 = sns.scatterplot(x=map_data["Population_(in_millions)"],y=map_data["Number_of_Imperiled_Species"],hue=map_data["Continent"]).set(xlabel="Population (in millions)",ylabel="Number of Imperiled Species",title="Imperiled Species by Country Population (Worldwide)")
#fig1.savefig("popXspecies_world.png")

#%% These graphs plot the number of imperiled species by population for the 10
# countries with the fewest number of imperiled species.
fig2 = sns.scatterplot(x=bottom_10["Population_(in_millions)"],y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Continent"]).set(xlabel="Population (in millions)",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Population\n(Displayed by Continent)")
#fig2.savefig("low10_popXspecies_cont.png")

fig3 = sns.scatterplot(x=bottom_10["Population_(in_millions)"],y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Country_or_Area"]).set(xlabel="Population (in millions)",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Population")
#fig3.savefig("low10_popXspecies.png")

#%% These graphs plot the number of imperiled species by population for the 10
# countries with the most imperiled species.
fig4 = sns.scatterplot(x=top_10["Population_(in_millions)"],y=top_10["Number_of_Imperiled_Species"],hue=top_10["Continent"]).set(xlabel="Popluation (in millions)",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Population\n(Displayed by Continent)")
#fig4.savefig("high10_popXspecies_cont.png")

fig5 = sns.scatterplot(x=top_10["Population_(in_millions)"],y=top_10["Number_of_Imperiled_Species"],hue=top_10["Country_or_Area"]).set(xlabel="Population (in millions)",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Population")
#fig5.savefig("high10_popXspecies.png")

#%% This graph plots the number of species by country land area (worldwide).
fig6 = sns.scatterplot(x=map_data["Land_Area_(thousand_hectares)"],y=map_data["Number_of_Imperiled_Species"],hue=map_data["Continent"]).set(xlabel="Land Area (thousand hectares)",ylabel="Number of Imperiled Species",title="Imperiled Species by Country Land Area (Worldwide)")
#fig6.savefig("areaXspecies_world.png")

#%% These graphs plot the number of imperiled species by country land area for
#   the 10 countries with the fewest number of imperiled species.
fig7 = sns.scatterplot(x=bottom_10["Land_Area_(thousand_hectares)"],y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Continent"]).set(xlabel="Land Area (thousand hectares)",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Land Area\n(Displayed by Continent)")
#fig7.savefig("low10_areaXspecies_cont.png")

fig8 = sns.scatterplot(x=bottom_10["Land_Area_(thousand_hectares)"],y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Country_or_Area"]).set(xlabel="Land Area (thousand hectares)",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Land Area")
#fig8.savefig("low10_areaXspecies.png")

#%% These graphs plot the number of imperiled species by country land area for
#   the 10 countries with the most imperiled species.
fig9 = sns.scatterplot(x=top_10["Land_Area_(thousand_hectares)"],y=top_10["Number_of_Imperiled_Species"],hue=top_10["Continent"]).set(xlabel="Land Area (thousand hectares)",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Land Area\n(Displayed by Continent)")
#fig9.savefig("high10_areaXspecies_cont.png")

fig10 = sns.scatterplot(x=top_10["Land_Area_(thousand_hectares)"],y=top_10["Number_of_Imperiled_Species"],hue=top_10["Country_or_Area"]).set(xlabel="Land Area (thousand hectares)",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Land Area")
#fig10.savefig("high10_areaXspecies.png")

#%% This graph plots the number of species by country income group (worldwide).
fig11 = sns.boxenplot(y=map_data["Income_Group"].sort_values(),x=map_data["Number_of_Imperiled_Species"]).set(xlabel="Number of Imperiled Species",ylabel="Income Group",title="Imperiled Species by Country Income Group (Worldwide)")
#fig11.savefig("incomeXspecies_world.png")

#%% These graphs plot the number of imperiled species by country income group for
#   the 10 countries with the fewest number of imperiled species.
fig12 = sns.scatterplot(x=bottom_10["Income_Group"].sort_values(),y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Continent"]).set(xlabel="Income Group",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Income Group\n(Displayed by Continent)")
#fig12.savefig("low10_incomeXspecies_cont.png")

fig13 = sns.scatterplot(x=bottom_10["Income_Group"].sort_values(),y=bottom_10["Number_of_Imperiled_Species"],hue=bottom_10["Country_or_Area"]).set(xlabel="Income Group",ylabel="Number of Imperiled Species",title="10 Countries with the Fewest Number of Imperiled Species by Country Income Group")
#fig13.savefig("low10_incomeXspecies.png")

#%% These graphs plot the number of imperiled species by country income group for
#   the 10 countries with the most imperiled species.
fig14 = sns.scatterplot(x=top_10["Income_Group"].sort_values(),y=top_10["Number_of_Imperiled_Species"],hue=top_10["Continent"]).set(xlabel="Income Group",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Income Group\n(Displayed by Continent)")
#fig14.savefig("high10_incomeXspecies_cont.png")

fig15 = sns.scatterplot(x=top_10["Income_Group"].sort_values(),y=top_10["Number_of_Imperiled_Species"],hue=top_10["Country_or_Area"]).set(xlabel="Income Group",ylabel="Number of Imperiled Species",title="10 Countries with the Most Imperiled Species by Country Income Group")
#fig15.savefig("high10_incomeXspecies.png")

#%% Now I'm done with coding and analyses. The remainder of my project involves
#   mapping in QGIS.