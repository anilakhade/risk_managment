import pandas as pd 

url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'

df = pd.read_json(url)

print(df.info())

