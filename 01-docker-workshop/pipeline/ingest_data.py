# get_ipython().system('uv add sqlalchemy psycopg2-binary tqdm')

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

year = 2021
month = 1

prefix = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
path = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

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
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

target_table = 'yellow_taxi_data'
chunk_size = 100000

def run():
    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'
    
    engine = create_engine(url=f"postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
    
    df_iter = pd.read_csv(path, dtype = dtype, parse_dates = parse_dates, iterator = True, chunksize = chunk_size)

    first = True

    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name=target_table,
                if_exists = "replace",
                con = engine)
            first = False

        df_chunk.to_sql(
            name = target_table,
            if_exists = "append",
            con = engine)

if __name__ == "__main__":
    run()