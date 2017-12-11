all: move2results

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

move2results: report
	mv src/R_analysis/generate_report.md results/finalreport/
	mv src/R_analysis/generate_report.html results/finalreport/
	mv src/R_analysis/generate_report results/finalreport/

clear_all:
	rm -f data/processed_data/*.csv
	rm -f data/*.csv
	rm -f results/*.png
	rm -f results/summary_tables/*.csv
	rm -f src/R_analysis/generate_report/*.png

