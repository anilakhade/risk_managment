import pandas as pd

SCRIP_MASTER_URL = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
OLD_XLSX = "OLD_DF.xlsx"

bro_df = pd.read_json(SCRIP_MASTER_URL)

print(bro_df[bro_df["name"] == "TATASTEEL"])
print(bro_df[bro_df["name"] == "NIFTY"])
