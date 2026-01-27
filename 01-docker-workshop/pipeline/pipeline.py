import sys
import pandas as pd

months_num = sys.argv[1]

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df["months"] = months_num

df.to_parquet(f"output_{months_num}.parquet")

print(df)