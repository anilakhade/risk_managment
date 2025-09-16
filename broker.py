import pandas as pd
import numpy as np


SCRIP_MASTER_URL = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
bro_df = pd.read_json(SCRIP_MASTER_URL)


df = pd.read_excel("OLD_DF.xlsx")
df["EXPIRY"] = pd.to_datetime(df["EXPIRY"], errors='coerce')
df["EXPIRY"] = df["EXPIRY"].dt.strftime("%d%b%Y").str.upper()
df["EXPIRY"] = df["EXPIRY"].fillna("")
df["OPT_TYPE"] = df["OPT_TYPE"].fillna("")
df["STRIKE"] = pd.to_numeric(df["STRIKE"], errors='coerce').fillna(0).astype(float)

print(bro_df[bro_df["instrumenttype"] == "FUTCOM"])
#print(df.head())

df1 = df.copy()
conditions = [
    df1["INSTRUMENT"].isin(["OPTSTK", "OPTIDX", "OPTFUT"]),
    df1["INSTRUMENT"].isin(["FUTCOM", "FUTSTK", "FUTIDX"])
]

choices = [
    df1["OPT_TYPE"].astype(str).str.upper(),
    "FUT"
]

df1["type"] = np.select(conditions, choices, default="")
df1["new_strike"] = (df1["STRIKE"]*100).astype(int)


#print(df1)
