# A script that generated data for hypothesis testing. 
# 
# Date: December 2017
# 
# Author: Simran Sethi
# 
# This script establishes a sqlite database connetion and then loads all the csv's from the data folder 
# and stores them into the /data/processed_data folder after processing over them.
# 
# usage: input = data/*.csv
#        output = data/processed_data/*.csv
# This .py file has been downloaded from the ipython notebook (src/createtables.ipynb)




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
import warnings
warnings.filterwarnings('ignore')



conn = sqlite3.connect('data/data.db')



# testing connetion to SQL database
country = pd.read_sql(
    """
    select * from country
    """, con = conn
)
country.head(4)



# creating summary statistic on the above table

region_summary = pd.read_sql("""
    select Region, count(*) as Count
    from country
    group by Region
    order by 2 desc
""",con = conn)


region_summary.to_csv('results/summary_tables/region_summary.csv')



# Let's do a LEFT JOIN on some subqueries 
source_of_most_recent_income_and_expenditure = pd.read_sql(
        """ 
           
            SELECT      A.CountryCode
                        ,B.LatestPopulationCensus
                        ,B.SourceOfMostRecentIncomeAndExpenditureData
                        ,B.ShortName
            FROM       ( 
                            -- First subquery (i.e the Left table)
                            
                           SELECT      CountryCode
                                        ,LatestPopulationCensus
                                        ,SourceOfMostRecentIncomeAndExpenditureData
                                        ,ShortName
                           FROM        Country
                        ) AS A
            LEFT JOIN   (
                            -- Second subquery (i.e the right table )
                            
                            SELECT      CountryCode
                                        ,LatestPopulationCensus
                                        ,SourceOfMostRecentIncomeAndExpenditureData
                                        ,ShortName
                            FROM        Country AS A
                            
                          ) AS B
            ON          A.CountryCode = B.CountryCode    
            
        """, con=conn)

source_of_most_recent_income_and_expenditure.to_csv('results/summary_tables/source_of_most_recent_income_and_expenditure.csv')



distinct_indicator_names_and_codes = pd.read_sql(
        """ 
           
            select distinct SeriesCode, IndicatorName
            from series
        """, con=conn)

distinct_indicator_names_and_codes.to_csv('results/summary_tables/distinct_indicator_names_and_codes.csv')


# *************************** Generating data for testing and results ****************************
# 
# I shall now select the indicators relevant to our analysis as the full table contains too many Indicators to choose from.
# 
# A quick description of the indicators is as follows:
# 
# - Hypothesis 1
# 
# `EN.ATM.CO2E.PC` = CO2 emissions (metric tons per capita)
# 
# `EN.ATM.PM25.MC.M3` = PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)
# 
# - Hypothesis 2
# 
# `SP.DYN.LE00.IN` = Life expectancy at birth, total (years)
# 
# `NY.GDP.PCAP.CD` = GDP per capita (current US$)
# 
# - Hypothesis 3
# 
# `SH.MED.BEDS.ZS` = Hospital beds (per 1,000 people)
# 
# `SP.DYN.AMRT.MA` = Mortality rate, adult, male (per 1,000 male adults)

# generates data/processed_data/hypothesis1.csv
hypothesis1 = pd.read_sql(""" SELECT   * 
                             FROM     Indicators 
                             WHERE    IndicatorCode IN 
                                      ( 'EN.ATM.CO2E.PC','EN.ATM.PM25.MC.M3')
                            order by CountryName,Year
                        """, con=conn)
hypothesis1.to_csv('data/processed_data/hypothesis1.csv')


# generates data/processed_data/hypothesis1_2010.csv
hypothesis1_2010 = pd.read_sql(""" SELECT   t1.CountryName as CountryName, t1.CountryCode as CountryCode,t1.Year as year,t1.IndicatorName as IndicatorName1,t2.IndicatorName as IndicatorName2,t1.IndicatorCode as IndicatorCode1, t2.IndicatorCode as IndicatorCode2,t1.Value as Value1,t2.Value as Value2 from
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'EN.ATM.CO2E.PC') and Year = 2010) as t1,
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'EN.ATM.PM25.MC.M3') and Year = 2010) as t2
                where t1.CountryCode = t2.CountryCode
            """, con=conn)

hypothesis1_2010.to_csv('data/processed_data/hypothesis1_2010.csv')


# generates data/processed_data/hypothesis2.csv
hypothesis2 = pd.read_sql(""" SELECT   * 
                             FROM     Indicators 
                             WHERE    IndicatorCode IN 
                                      ( 'SP.DYN.LE00.IN','NY.GDP.PCAP.CD')
                            order by CountryName,Year
                        """, con=conn)
hypothesis2.to_csv('data/processed_data/hypothesis2.csv')


# generates data/processed_data/hypothesis2_2010.csv
hypothesis2_2010 = pd.read_sql(""" SELECT   t1.CountryName as CountryName, t1.CountryCode as CountryCode,t1.Year as year,t1.IndicatorName as IndicatorName1,t2.IndicatorName as IndicatorName2,t1.IndicatorCode as IndicatorCode1, t2.IndicatorCode as IndicatorCode2,t1.Value as Value1,t2.Value as Value2 from
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'SP.DYN.LE00.IN') and Year = 2010) as t1,
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'NY.GDP.PCAP.CD') and Year = 2010) as t2
                where t1.CountryCode = t2.CountryCode
            """, con=conn)

hypothesis2_2010.to_csv('data/processed_data/hypothesis2_2010.csv')


# generates data/processed_data/hypothesis3.csv
hypothesis3 = pd.read_sql(""" SELECT   * 
                             FROM     Indicators 
                             WHERE    IndicatorCode IN 
                                      ( 'SH.MED.BEDS.ZS','SP.DYN.AMRT.MA')
                            order by CountryName,Year
                        """, con=conn)
hypothesis3.to_csv('data/processed_data/hypothesis3.csv')


# generates data/processed_data/hypothesis3_2010.csv
hypothesis3_2010 = pd.read_sql(""" SELECT   t1.CountryName as CountryName, t1.CountryCode as CountryCode,t1.Year as year,t1.IndicatorName as IndicatorName1,t2.IndicatorName as IndicatorName2,t1.IndicatorCode as IndicatorCode1, t2.IndicatorCode as IndicatorCode2,t1.Value as Value1,t2.Value as Value2 from
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'SH.MED.BEDS.ZS') and Year = 2010) as t1,
                (select * FROM     Indicators WHERE    IndicatorCode IN ( 'SP.DYN.AMRT.MA') and Year = 2010) as t2
                where t1.CountryCode = t2.CountryCode
            """, con=conn)

hypothesis3_2010.to_csv('data/processed_data/hypothesis3_2010.csv')

