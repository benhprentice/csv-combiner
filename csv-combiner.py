import sys
import pandas as pd


files = []

for arg in range(1, len(sys.argv)):
    df = pd.read_csv(sys.argv[arg])
    filename = sys.argv[arg].split('/')
    filename = filename[-1]
    df['filename'] = filename
    files.append(df)
if files != None:
       combined_csv = pd.concat(f for f in files)
combined_csv.to_csv(sys.stdout, index=False)