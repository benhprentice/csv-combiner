import pandas as pd

def combineCsv(files):
    combined_csv = pd.concat(f for f in files)
    return combined_csv