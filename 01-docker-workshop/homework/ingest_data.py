
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

engine = create_engine("postgresql+psycopg2://root:root@localhost:5432/nov_taxi")

green_tripdata_path = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
zones_path = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

green_trips_df = pd.read_parquet(
    path = green_tripdata_path,
    engine = "pyarrow",
)

dtype = {
    "LocationID": "Int64",
    "Borough": "string",
    "Zone": "string",
    "Service": "string"
}

zones_df = pd.read_csv(zones_path, dtype = dtype, iterator = True, chunksize = 100)

green_trips_df.to_csv("data/green_trip.csv", index = False)

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime"
]

df_iter_green = pd.read_csv(
    "data/green_trip.csv",
    dtype = dtype,
    parse_dates = parse_dates,
    iterator = True,
    chunksize = 10000
)

df = pd.read_csv("data/green_trip.csv", dtype=dtype, parse_dates=parse_dates)

print(pd.io.sql.get_schema(frame = df, name = "test", con = engine))

first = True

for df_chunk in tqdm(df_iter_green):
    if first:
        df_chunk.head(0).to_sql(name = "nov_trips", if_exists = "replace", con = engine)
        first = False
        print("Table Created!!!")
    df_chunk.to_sql(name = "nov_trips", if_exists = "append", con = engine)
    print("Inserted:",len(df_chunk))        

first = True

for df_chunk in tqdm(zones_df):
    if first:
        df_chunk.head(0).to_sql(name = "nov_zones", if_exists = "replace", con = engine)
        first = False
        print("Table Created!!!")
    df_chunk.to_sql(name = "nov_zones", if_exists = "append", con = engine)
    print("Inserted:",len(df_chunk))        


