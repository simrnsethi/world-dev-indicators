**Note**: Run the "src/download_data.py" script to generate data files. (`make all` command automatically does that)


### The desciption of the processed data is as follows:


#### A quick description of the indicators codes:

 - Hypothesis 1

 	- `EN.ATM.CO2E.PC` = CO2 emissions (metric tons per capita)

 	- `EN.ATM.PM25.MC.M3` = PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)

 - Hypothesis 2

	- `SP.DYN.LE00.IN` = Life expectancy at birth, total (years)

 	- `NY.GDP.PCAP.CD` = GDP per capita (current US$)

- Hypothesis 3

	- `SH.MED.BEDS.ZS` = Hospital beds (per 1,000 people)

	- `SP.DYN.AMRT.MA` = Mortality rate, adult, male (per 1,000 male adults)

**hypothesis1.csv, hypothesis2.csv, hypothesis3.csv contain the following columns:**

|   Column Name	|  Column Description 	|
|---	|---	|
|   CountryName	|   The name of the country out of 219 countries in this dataset	|
|   CountryCode	|   Short country code	|
|   IndicatorName	|   Name of the indicator	|
|   IndicatorCode	|   Code of the indicator	|
|   Year	|   From 1960 to 2011	|
|   Value	|   Value of the indicator	|

> hypothesis1_2010.csv, hypothesis2_2010.csv, hypothesis3_2010.csv contain the above columns filtered for the Year 2010