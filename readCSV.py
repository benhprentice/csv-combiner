import sys
import pandas as pd

def readCsv():
    files = []

    for arg in range(1, len(sys.argv)):
        df = pd.read_csv(sys.argv[arg])
        filename = sys.argv[arg].split('/')
        filename = filename[-1]
        df['filename'] = filename
        files.append(df)
    return files
