import pandas as pd
import zipfile
import requests
import io

# Extracting Indicators zip file and storing it as a csv in /data folder
indicators_zip_file = 'https://storage.googleapis.com/data-world-dev/Indicators.csv.zip'
r = requests.get(indicators_zip_file)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('data/')	

# Extracting Series zip file (Note: a zip file need not have .zip as an extension)
series_zip_file = 'https://storage.googleapis.com/data-world-dev/Series.csv'
r = requests.get(series_zip_file)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('data/')	

# Extracting Footnotes zip file (Note: a zip file need not have .zip as an extension)
footnotes_zip_file = 'https://storage.googleapis.com/data-world-dev/Footnotes.csv'
r = requests.get(footnotes_zip_file)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('data/')

# Extracting Country csv
country = pd.read_csv('https://storage.googleapis.com/data-world-dev/Country.csv')
country.to_csv('data/Country.csv',index = False)

# Extracting SeriesNotes csv
country = pd.read_csv('https://storage.googleapis.com/data-world-dev/SeriesNotes.csv')
country.to_csv('data/SeriesNotes.csv',index = False)

# Extracting Series Notes csv
country = pd.read_csv('https://storage.googleapis.com/data-world-dev/CountryNotes.csv')
country.to_csv('data/CountryNotes.csv',index = False)



