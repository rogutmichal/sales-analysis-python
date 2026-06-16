import pandas as pd

# wczytanie danych
df = pd.read_csv("data/sales.csv")

print(df.head())
print(df.info())