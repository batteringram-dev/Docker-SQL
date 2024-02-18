#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd
from time import time
from sqlalchemy import create_engine



def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # converting our parquet to csv
    #pf = ParquetFile('yellow_tripdata_2023-01.parquet')

    #df = pf.to_pandas()

    #df.to_csv('yellow_taxi_data.csv')

    df_iter = pd.read_csv('yellow_taxi_data.csv', iterator = True, chunksize = 100000)

    df = next(df_iter)

    df.drop(columns = ['Unnamed: 0'], inplace = True)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name = table_name, con = engine, if_exists = 'replace')

    df.to_sql(name = table_name, con = engine, if_exists = 'append')


    while True:

        t_start = time()
    
        df = next(df_iter)
    
        df.drop(columns = ['Unnamed: 0'], inplace = True)
    
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
        df.to_sql(name = table_name, con = engine, if_exists = 'append')
    
        t_end = time()
    
        total_time = t_end - t_start
    
        print(f'inserted a new chunk... took {total_time} seconds')


if __name__ == '__main__':
    parser = argparse.ArguementParser(description = 'Ingest CSV data to Postgres')

    parser.add_arguement('--user', help = 'user name for postgres')
    parser.add_arguement('--password', help = 'password for postgres')
    parser.add_arguement('--host', help = 'host for postgres')
    parser.add_arguement('--port', help = 'port for postgres')
    parser.add_arguement('--db', help = 'database name for postgres')
    parser.add_arguement('--table_name', help = 'table name for postgres')

    args = parser.parse_args()

    main(args)








