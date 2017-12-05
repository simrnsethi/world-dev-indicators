library("tidyverse")

options(warn = -1)

#importing and exploring Country.csv
country  = read_csv('data/Country.csv')
head(country)
str(country)

#importing and exploring CountryNotes.csv
countrynotes  = read_csv('data/CountryNotes.csv')
head(countrynotes)
str(countrynotes)

#importing and exploring Footnotes.csv
footnotes  = read_csv('data/Footnotes.csv')
head(footnotes)
str(footnotes)

#importing and exploring Indicators.csv
indicators  = read_csv('data/Indicators.csv')
head(indicators)
str(indicators)

#importing and exploring Series.csv
series  = read_csv('data/Series.csv')
head(series)
str(series)

#importing and exploring SeriesNotes.csv
series_notes  = read_csv('data/SeriesNotes.csv')
head(series_notes)
str(series_notes)

options(warn = 0)
