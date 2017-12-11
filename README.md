# World Development Indicators Analysis
A repository to analyze world development indicators 🌎

The World Development Indicators from the World Bank contain over a thousand annual indicators of economic development from hundreds of countries around the world.

## Questions ❓

> Is higher percentage of Rural population (% of total population) in a country linked to less Agricultural machines (tractors)? Or is the reverse true? 
> 
> Does higher Merchandise exports by the reporting economy (current USD) imply a larger GDP per capita (current USD) of a country?

These are some of the questions to which I want to seek answers through this dataset provided by the world bank.

I plan to make my analysis reproducible so as to ease the tasks of those contributors interested in helping me expand the set of questions that can be asked given this dataset.

In the end I will provide some plots and figures which can be interepreted in the context of the intended hypotheses questions.

## Hypotheses 🔍

The following hypotheses will be tested (list will be expanded):

1. _More_ CO2 emissions from gaseous fuel consumption (% of total) leads to _more_  SP2.5 particulate matter in the air (Annually).
2. _Higher_ life expectancy at birth is true for countries with _higher_ GDP (in US$)
3. _More_ Hospital beds (per 1,000 people) leads to _lower_ mortality rates.

## Data Sources 📂

The data is taken from [Kaggle's World Development Indicator Dataset](https://www.kaggle.com/worldbank/world-development-indicators/data) for the convenince of the contributors I have stored the data on Google Cloud Buckets. This can easily be downloaded by running `download_data.py` python script in `/src` folder. This data has been provided by the worldbank.

Released Under [**World Bank Dataset Terms of Use**](http://web.worldbank.org/WBSITE/EXTERNAL/0,,contentMDK:22547097~pagePK:50016803~piPK:50016805~theSitePK:13,00.html).

1. [Country.csv](https://storage.googleapis.com/data-world-dev/Country.csv): This data file has information regarding the different parameters on which all the countries in this dataset have been classified by worldbank.
2. [CountryNotes.csv](https://storage.googleapis.com/data-world-dev/CountryNotes.csv): This datafile has country codes, series codes(info in Series.csv) and a description of the data source for each country.
3. [Footnotes.csv](https://storage.googleapis.com/data-world-dev/Footnotes.csv): This file is an expanded version of the previous file where each data source row is further split into rows for each year for which the data is present for that particular country.
4. [Indicators.csv.zip](https://storage.googleapis.com/data-world-dev/Indicators.csv.zip): This is the main file of interest which has the information regarding the data values for different indicators on each countries development has been measured.
5. [Series.csv](https://storage.googleapis.com/data-world-dev/Series.csv): This file has series codes (found in country notes) description.
6. [SeriesNotes.csv](https://storage.googleapis.com/data-world-dev/SeriesNotes.csv): This file has further year-wise expanded information on the data found in the Series.csv file.



## Data Analysis Plan 📋

- Clean and structurize the data.
- Run hypothesis tests on the above mentioned hypothesis (maybe paired t-test or ANOVA?).
- Represent the final results in the form of graphs and figures.
- Document the findings from the dataset.

## How to run the analysis ⚙️

1. Clone this repo to a local folder on your system.
2. Navigate into this folder "world-dev-indicators" through command line.
3. Type:
			
		
		$make clear_all
			
		
	This will clear all the result files which come with this repo.

4. Now, type:

		
		$make all
		
This will run all the scripts in the `src/` folder as per the sequence in `Makefile` and render the analysis in the `results/` folder.

The final report is rendered at this location: `results/finalreport/`