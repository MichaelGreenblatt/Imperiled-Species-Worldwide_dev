# International-Effects-of-Agriculture-on-Wildlife_dev

# Background
Nearly every country in the world has legal protections for imperiled species (threatened or endangered species). These laws primarily originate from obligations from the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES), which is the international treaty that regulates protections for imperiled species. Beyond the base requirements of CITES, however, some countries have their own rules to protect imperiled species. Thus, some countries have more stringent protections than others. Likewise, some countries may extend protections to additional species beyond those protected by CITES.

The map below shows the number of imperiled species per country worldwide:
![Map 1_Imperiled Species per Country](https://user-images.githubusercontent.com/98333734/167975070-19345260-efc4-4855-b2f7-651e2722ee5d.png)

For this project, I analyze the number of species that are officially registered as imperiled for almost every country (and many territories) in the world. (Note: for convenience, since territories are included in the original data as if they're countries, country hereafter refers to any geographic entity that is treated as such in the data.) Specifically, I compare the number of imperiled species per country by countries' populations, land areas, and income groups. The purpose of these analyses is to investigate whether there are any associations between the number of imperiled species in a country and any of these characteristics.

# Data Sources
All of the data is sourced from the United Nations Statistics Division (data.un.org) except for the income group data, which comes from the World Bank's Development Data Group (data.worldbank.org), and the shapefile map data, which comes from IPUMS International (international.ipums.org). The exact source URLs and the names of the original files that I downloaded are described in the scripts when they are first imported.

# Outputs
There are 4 scripts produced in this project, as well as 15 graphs and a QGIS file with 7 maps.

All of the scripts should be run in the order indicated below. The number is also written at the top of each script for convenience. For the best results, each script should be read section-by-section, except for the graphs, which should be read line-by-line.

## Script #1: countries.py
This script imports most of the files to create a DataFrame of the variables that will be used as the basis for the analyses. Specifically, it imports files for the population, population density, land area, income group, and number of imperiled species variables. Each of those variables comes from a different file, except the population and population density variables are from the same file. The script also imports country number and country code variables, which are used for merges throughout this project. Finally, it also imports continent and region variables, which are used for categorizing countries geographically, and a country name variable so that we can see which country is being described.

In short, each of the variables is imported as a DataFrame, then each of the DataFrames are merged on the country code to create the master DataFrame called "merge_countries", which is then exported as a CSV file ("all_countries_data.csv").

## Script #2: map_info.py
Next, I constructed the map data that I use in QGIS. First, I reimported merge_countries. Then I imported the shapefile as a GeoDataFrame and merged both of these DataFrames into a new master GeoDataFrame called "map_data", which is the master DataFrame that I use for all of the analyses because it contains all of the variables that I want as well as all of the countries that will be mapped. Finally, I exported map_data as a GeoPackage ("map_data.gpkg") so that I could use it for mapping in QGIS.

## Script #3: continents.py
The last two scripts analyze the data. This script imports "map_data.gpkg" to categorize countries by continent and then visualize the population and population density of each country and the number of countries and the population of each continent. I also calculated the total number of countries worldwide and the global population. Lastly, I visualized each country's quintile for its number of imperiled species. All of these calculations, but especially the population numbers and the species quintiles, are for reference so that we can understand each country's statistics and visually compare countries. No output file is produced from this script.

## Script #4: graphs.py
I used this script to graph all of the variables for a more thorough analysis. Specifically, I created scatterplots of: (1) the species variable against country population, (2) species against country land area, and (3) species against country income group (one of the income group graphs is a boxenplot). For each of those comparisons, I created a worldwide scatterplot to see the global distribution of each variable, and I also created two scatterplots for the 10 countries with the most imperiled species and the 10 countries with the fewest imperiled species; one graph for each of these lists of countries is categorized by continent and the other is categorized by country. In other words, there are 5 graphs produced for each variable tested. There are 15 graphs in total.

## QGIS
After I finished coding, I created 7 maps in QGIS using the data in "map_data.gpkg". The QGIS file is "Imperiled_Species_Worldwide_Maps.qgz". The maps are as follows:

Map 1: Number of Imperiled Species per Country
Map 2: Country Populations
Map 3: Population Density per Country
Map 4: Land Area per Country
Map 5: Countries by Income Group
Map 6: Number of Imperiled Species by Country Population
Map 7: Number of Imperiled Species by Country Land Area

# Results & Discussion
![Map 6_Imperiled Species by Country Population](https://user-images.githubusercontent.com/98333734/167974929-3477d3d0-2af8-437b-b8b0-0a42b8e21aa3.png)
![Map 7_Imperiled Species by Country Land Areas](https://user-images.githubusercontent.com/98333734/167974831-17683bbd-e6f8-4ca6-89fa-61990b9e7dbd.png)
These analyses and maps lead to some conclusions. From the maps, we see that countries with the largest populations and the highest population densities tend to have the most imperiled species. More notable is that we see that land area and geography have even stronger results. Specifically, the countries clustered around the equator and between the Tropic of Cancer and the Tropic of Capricorn tend to have the most imperiled species, while the countries closer to the poles generally have fewer imperiled species. This makes sense biologically since biodiversity is richest near the equator. What's also interesting is that the countries with smaller land areas tend to have the most imperiled species, which also makes sense intuitively - this is particularly true in the island nations in the Carribbean and Oceania, but we also see it in the smaller countries of Europe, central Africa, and Central America.

Two outliers to note in the maps are Greenland, which has a small population and is categorized as high income, but it has a lot of imperiled species given its population, and India, which has a lot of imperiled species, a large population, and high population density, but its number of imperiled species given its population is small.

We see similar results in the graphs. Specifically, the number of imperiled species trends upward based on country population, while the worldwide trend is downward for land area. The worldwide trend for country income group is slightly bottom-heavy, although the countries with the largest number of imperiled species are generally clustered in the middle incomes; this could be an indication of industrialization, which is generally the most environmentally-destructive phase of economic development.

All of these results indicate that there are discernible patterns that are associated with a country having fewer or more imperiled species. It should be noted that the number of imperiled species is subjective and political in that the numbers in some countries (or all of them) may be artificially low. Likewise, only a minimal portion of species that are truly imperiled in the world are legally defined as such. Unfortunately, the data I used for this project doesn't address either of these potential biases. Therefore, while some countries may look like they're doing well and some countries may look like they're doing poorly, this analysis likely gives only a partial picture of each country's true circumstances.

Further research beyond this project could investigate the impacts to imperiled species of particular industries, the proportions of each country's population in urban and rural areas, the types of species that tend to get legal protections, the amount of protected habitat or land per country (especially as a percentage of the total land area), and political differences between countries that have strong and weak protections or countries that have a lot of imperiled species and countries that have fewer imperiled species.
