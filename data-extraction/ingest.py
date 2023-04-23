import argparse
import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = int(params.port)
    db = params.db
    table_name = params.table_name
    url = params.url
    output_csv = "data/raw/motogp.csv"

    print(f"File successfully downloaded. Now Loading it into databse........")
    # Insert the downloaded data into the database
    df = pd.read_csv(output_csv)
    print(df.head())
    url = URL.create("postgresql", username=user, password=password, host=host, database=db, port=port)
    engine = create_engine(url)
    print(f"Successfully created a connection to the db")
    # breakpoint()
    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest data into db")

    # user, password, host, port, db name, table name, parquet file url
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='url for parquet for postgres')

    # parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find max)')

    args = parser.parse_args()

    main(args)

# print(args.accumulate(args.integers))

