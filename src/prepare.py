import pandas as pd
pd.read_csv("data/raw.csv").dropna().to_csv("data/clean.csv", index=False)
