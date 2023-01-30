from readCSV import readCsv
from combineCSV import combineCsv
from saveCSV import saveCsv

files = readCsv()
combined_csv = combineCsv(files)
saveCsv(combined_csv)