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


df2 = df1.copy()

df2["SYMBOL"] = df2["SYMBOL"].fillna("").astype(str)
df2["EXPIRY"] = df2["EXPIRY"].fillna("").astype(str)
df2["new_strike"] = df2["new_strike"].fillna("").astype(str)
df2["type"] = df2["type"].fillna("").astype(str)
df2["INSTRUMENT"] = df2["INSTRUMENT"].fillna("").astype(str)
df2["new_strike"] = df2["new_strike"].str.replace(r"\.0$", "", regex=True)

opt_mask = df2["INSTRUMENT"].isin(["OPTIDX", "OPTSTK", "OPTFUT"])
fut_mask = df2["INSTRUMENT"].isin(["FUTIDX", "FUTSTK", "FUTCOM"])
eq_mask  = df2["type"] == "-EQ"
df2["script"] = ""

df2.loc[opt_mask, "script"] = (
    df2.loc[opt_mask, ["SYMBOL", "EXPIRY", "new_strike", "type"]]
      .agg("_".join, axis=1)
)

df2.loc[fut_mask, "script"] = (
    df2.loc[fut_mask, ["SYMBOL", "EXPIRY", "type"]]
      .agg("_".join, axis=1)
)

df2.loc[eq_mask, "script"] = df2.loc[eq_mask, ["SYMBOL", "type"]].agg("_".join, axis=1)
df2["script"] = df2["script"].str.replace(r"_+", "_", regex=True).str.strip("_")

broker = bro_df[bro_df["exch_seg"].isin(['NSE', 'NFO', 'MCX', 'BFO'])]
broker = broker.copy()

condition = [
    broker["symbol"].str.endswith("CE"),
    broker["symbol"].str.endswith("PE"),
    broker["symbol"].str.endswith("FUT"),
    broker["symbol"].str.endswith("-EQ"),
]

choice = ["CE", "PE", "FUT", "-EQ"]
broker["type"] = np.select(condition, choice, default="")

bro = broker.copy()

bro["expiry"] = bro["expiry"].fillna("").astype(str)
bro["strike"] = bro["strike"].fillna("").astype(str)
bro["type"] = bro["type"].fillna("").astype(str)

opt_mask  = bro["instrumenttype"].isin(["OPTIDX", "OPTSTK", "OPTFUT"])
fut_mask  = bro["instrumenttype"].isin(["FUTIDX", "FUTSTK", "FUTCOM"])
eq_mask = bro["type"] == "-EQ"

broker["script"] = ""

bro.loc[opt_mask, "script"] = (
    bro.loc[opt_mask, ["name", "expiry", "strike", "type"]]
    .agg("_".join, axis=1)
)

bro.loc[fut_mask, "script"] = (
    bro.loc[fut_mask, ["name", "expiry", "type"]]
    .agg("_".join, axis=1)
)

bro.loc[eq_mask, "script"] = bro.loc[eq_mask, "symbol"]
bro["script"] = bro["script"].str.replace(r'_+', '_', regex=True).str.strip("_")
bro["script"] = bro["script"].fillna("")
df2["script"] = df2["script"].astype(str).str.strip()
bro["script"] = bro["script"].astype(str).str.strip()

merged = df2.merge(
    bro[["script", "token"]],
    on="script",
    how="left",
    suffixes=("", "_bro")
)

merged["match"] = merged["token"].notna()
merged["token"] = merged["token"].fillna("")
df2 = merged
final_df = df2[[
    "match",
    "token",
    "script",
    "SYMBOL",
    "EXPIRY",
    "STRIKE",
    "OPT_TYPE"
]].copy()

final_df = final_df.drop_duplicates(subset=["script"], keep="first").reset_index(drop=True)
final_df.to_csv("final_df.csv")

