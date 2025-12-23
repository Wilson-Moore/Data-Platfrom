import pandas as pd
from dotenv import dotenv_values


ENV_KEYS=dotenv_values(".env")

df=pd.read_excel(f"{ENV_KEYS.get("FILES_PATH")}/shipping_rates.xlsx",engine="openpyxl")

print(df.head())