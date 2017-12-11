import csv
import glob
import sqlite3
import os
import pandas as pd

def file2table(db):
	filename1 = 'data/Indicators.csv'
	tablename1 = os.path.splitext(os.path.basename(filename1))[0].lower()
	df = pd.read_csv(filename1)
	df.to_sql(tablename1, conn, if_exists='replace', index=False)

	filename2 = 'data/Country.csv'
	tablename2 = os.path.splitext(os.path.basename(filename2))[0].lower()
	df = pd.read_csv(filename2)
	df.to_sql(tablename2, conn, if_exists='replace', index=False)

	filename3 = 'data/CountryNotes.csv'
	tablename3 = os.path.splitext(os.path.basename(filename3))[0].lower()
	df = pd.read_csv(filename3)
	df.to_sql(tablename3, conn, if_exists='replace', index=False)

	filename4 = 'data/Footnotes.csv'
	tablename4 = os.path.splitext(os.path.basename(filename4))[0].lower()
	df = pd.read_csv(filename4)
	df.to_sql(tablename4, conn, if_exists='replace', index=False)

	filename5 = 'data/Series.csv'
	tablename5 = os.path.splitext(os.path.basename(filename5))[0].lower()
	df = pd.read_csv(filename5)
	df.to_sql(tablename5, conn, if_exists='replace', index=False)

	filename6 = 'data/SeriesNotes.csv'
	tablename6 = os.path.splitext(os.path.basename(filename6))[0].lower()
	df = pd.read_csv(filename6)
	df.to_sql(tablename6, conn, if_exists='replace', index=False)


if __name__ == '__main__':
	conn = sqlite3.connect('data/data.db')
	file2table(conn)



