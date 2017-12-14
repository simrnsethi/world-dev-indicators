# Driver Makefile 
# Date: 10 December 2017
# Author: Simran Sethi
# This is the master makefile which runs all the other scripts. 
# Please refer to the dependency diagram here: https://github.com/simrnsethi/world-dev-indicators/blob/master/Makefile.png
# usage: $make clear_all 
# 		 $make all

all: move2doc

# downloads the data from google cloud API
download_data:
	python src/download_data.py

# Converts the CSVs to SQL databases
csv2db: download_data
	python src/Python_analysis/csv2db.py

# generates analysis tables and summary tables
create_tables: csv2db
	python src/Python_analysis/createtables.py

# generates final report in 
report: create_tables
	Rscript -e "ezknitr::ezknit('src/R_analysis/generate_report.Rmd')"

move2doc: report
	mv src/R_analysis/generate_report.md doc/final_report/
	mv src/R_analysis/generate_report.html doc/final_report/
	mv src/R_analysis/generate_report doc/final_report/

clear_all:
	rm -f data/processed_data/*.csv
	rm -f data/*.csv
	rm -f results/*.png
	rm -f results/summary_tables/*.csv
	rm -f src/R_analysis/generate_report/*.png

