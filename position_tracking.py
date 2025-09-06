import pandas as pd
import numpy as np

new_df = pd.read_excel("NEW_DF.xlsx")
old_df = pd.read_excel("OLD_DF.xlsx")

new_df = new_df.copy()
for col in ["BUY_QTY", "SELL_QTY"]:
    new_df[col] = pd.to_numeric(new_df[col], errors='coerce').fillna(0).astype("int64")

for col in ["BUY_RATE", "SELL_RATE"]:
    new_df[col] = pd.to_numeric(new_df[col], errors='coerce').fillna(0).astype("float64")

old_df = old_df.copy()
old_df["QUANTITY"] = pd.to_numeric(old_df["QUANTITY"], errors='coerce').fillna(0)

for df in [new_df, old_df]:
    df["EXPIRY"] = pd.to_datetime(df["EXPIRY"], errors='coerce')
    df["EXPIRY"] = df["EXPIRY"].dt.strftime("%d%b%y").str.upper()
    df["EXPIRY"] = df["EXPIRY"].fillna("")
    df["OPT_TYPE"] = df["OPT_TYPE"].fillna("")
    df["STRIKE"] = pd.to_numeric(df["STRIKE"],errors='coerce').astype("float64")

df1 = new_df.copy()

df1["QUANTITY"] = (df1["BUY_QTY"] - df1["SELL_QTY"]).fillna(0).astype("int64")
df1["RATE"] = np.where(df1["BUY_QTY"] > 0, df1["BUY_RATE"], df1["SELL_RATE"])
df1["BOOKED_QTY"] = np.minimum(df1["BUY_QTY"], df1["SELL_QTY"])

keys = [
    "BROKER_ID", "SHEET", "STRATEGY",
    "EXCHANGE", "INSTRUMENT", "SYMBOL", "EXPIRY", "STRIKE", "OPT_TYPE",
    "BOOKED_QTY","BUY_RATE", "SELL_RATE"
]

intra_booked = df1[keys].copy()
intra_booked = intra_booked[intra_booked["BOOKED_QTY"] != 0].copy()


key2 = [
    "BROKER_ID", "SHEET", "STRATEGY",
    "EXCHANGE", "INSTRUMENT", "SYMBOL", "EXPIRY", "STRIKE", "OPT_TYPE",
    "QUANTITY", "RATE"
]

df2 = df1[key2].copy()
df2 = df2[df2["QUANTITY"] != 0].copy() #this is intraday outstanding position

df3 = old_df.copy() # this is old net position

key3 = [
    "BROKER_ID", "SHEET", "STRATEGY",
    "EXCHANGE", "INSTRUMENT", "SYMBOL", "EXPIRY", "STRIKE", "OPT_TYPE",
]

df = pd.concat([df2, df3], axis=0, ignore_index=True) # this is total of df2 and df3
dup = df[df.duplicated(subset=key3, keep=False)].copy()
df = df.drop(dup.index).reset_index(drop=True)
booked_df_parts = []

for _, grp in dup.groupby(key3, sort=False):
    if grp["QUANTITY"].sum() == 0:
        booked_df_parts.append(grp)

booked_df = pd.concat(booked_df_parts, ignore_index=True)

dup = dup.merge(booked_df, how="outer", indicator=True).query('_merge == "left_only"').drop(columns="_merge").reset_index(drop=True)

booked_partial = []
open_partial = []

for _, grp in dup.groupby(key3, sort=False):
    pos = grp[grp["QUANTITY"] > 0]
    neg = grp[grp["QUANTITY"] < 0]

    if pos.empty or neg.empty:
        open_partial.append(grp.copy())
        continue

    # Total quantities
    q_pos = pos["QUANTITY"].sum()
    q_neg = neg["QUANTITY"].sum()  # negative

    # Matched quantity
    book_qty = min(q_pos, -q_neg)

    # BOOKED rows
    pos_booked = pos.iloc[0].copy()
    neg_booked = neg.iloc[0].copy()
    pos_booked["QUANTITY"] = book_qty
    neg_booked["QUANTITY"] = -book_qty
    booked_partial.extend([pos_booked.to_frame().T, neg_booked.to_frame().T])

    # OPEN leftover
    if q_pos > book_qty:
        leftover = pos.iloc[0].copy()
        leftover["QUANTITY"] = q_pos - book_qty
        open_partial.append(leftover.to_frame().T)

    if -q_neg > book_qty:
        leftover = neg.iloc[0].copy()
        leftover["QUANTITY"] = q_neg + book_qty  # still negative
        open_partial.append(leftover.to_frame().T)


# Combine booked positions
booked_df = pd.concat([booked_df] + booked_partial, ignore_index=True)

# Combine remaining unmatched positions
left_par_df = pd.concat(open_partial, ignore_index=True)

def collapse_positions(df, key3):
    grouped = df.groupby(key3, sort=False)
    result = []

    for group_keys, group_df in grouped:
        qty_sum = group_df["QUANTITY"].sum()
        vwap = (group_df["QUANTITY"] * group_df["RATE"]).sum() / qty_sum

        result.append(dict(zip(key3, group_keys)) | {
            "QUANTITY": qty_sum,
            "RATE": vwap
        })

    return pd.DataFrame(result)

collapsed_left_par_df = collapse_positions(left_par_df, key3)


final_df = pd.concat([df, collapsed_left_par_df], ignore_index=True)
final_df.duplicated(subset=key3, keep=False).any()

intra_booked.to_csv("intraday_booked.csv", index=False)
final_df.to_csv("NET_POSITION.csv", index=False)
booked_df.to_csv("BOOKED_POSITION.csv", index=False)













