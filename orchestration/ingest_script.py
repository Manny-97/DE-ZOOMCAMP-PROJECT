import pandas as pd
import pycountry
from prefect import flow, task
from prefect_sqlalchemy import SqlAlchemyConnector


@task(name="transform", log_prints=True)
def transform(df):
    df = df.dropna(axis=0)
    df["country"] = df.country.apply(lambda x: pycountry.countries.get(alpha_2=x).name)
    return df


@task(name="ingest", log_prints=True, retries=3)
def ingest_data(table_name: str, df: pd.DataFrame):
    connection_block = SqlAlchemyConnector.load("ingest-motogp")
    with connection_block.get_connection(begin=False) as engine:
        print(pd.io.sql.get_schema(df, name=table_name, con=engine))
        df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")
        df.to_sql(name=table_name, con=engine, if_exists="append")
        query = """
        SELECT *
        FROM motogp
        LIMIT 100;
        """
        print(pd.read_sql(query, con=engine))


@flow(name="Test prefect")
def main(table_name: str):
    df = pd.read_csv("./data-extraction/data/raw/motogp.csv")
    data = transform(df)
    ingest_data(table_name, data)


if __name__ == "__main__":
    main(table_name="motogp")
