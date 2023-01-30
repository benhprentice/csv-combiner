import sys

def saveCsv(combined_csv):
    combined_csv.to_csv(sys.stdout, index=False)