import os
from pathlib import Path

import pandas as pd
import redshift_connector
from prefect import flow, task
from prefect_aws.s3 import S3Bucket


@task(retries=3)
def extract_from_s3():
    """ """
    s3_path = "data"
    s3_block = S3Bucket.load("moto-gp")
    local_path = Path(__file__).parent / "data"
    s3_block.get_directory(from_path=s3_path, local_path=local_path)

    return local_path


@task()
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning example"""
    full_path = os.path.join(path, "motogp.parquet")
    df = pd.read_parquet(full_path)
    print(df.head())
    return df


def map_df_dtypes_to_sql(dtype):
    if dtype == "float64":
        return "FLOAT"
    elif dtype == "int64":
        return "BIGINT"
    elif dtype == "object":
        return "VARCHAR(50)"
    elif dtype == "datetime64[ns]":
        return "TIMESTAMP"
    else:
        return "VARCHAR(50)"


@task(retries=3)
def write_to_redshift(df: pd.DataFrame) -> None:
    """ """
    # # ATTEMPT 1: use this aws python connector to connect to an existing cluster: https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html
    # # In case you encounter error accessing redshift, use this link: https://stackoverflow.com/questions/58399974/redshift-not-connecting-to-host-via-python-script

    user_redshift = os.environ.get("user_redshift")
    password_redshift = os.environ.get("password_redshift")
    redshift_host = os.environ.get("redshift_host")
    db_redshift = "dev"
    with redshift_connector.connect(
        host=redshift_host,
        database=db_redshift,
        port=5439,
        user=user_redshift,
        password=password_redshift,
    ) as conn:
        # Turn on autocommit
        conn.autocommit = True
        with conn.cursor() as cursor:
            # Create an empty table
            cursor.execute(
                "create table motogp (name varchar, season timestamp, country varchar, circuit varchar, constructor varchar, ride_class varchar)"
            )

            # Use COPY to copy the contents of the S3 bucket into the empty table
            cursor.execute(
                "copy motogp from 's3://motogp/data/motogp.csv' iam_role 'arn:aws:iam::123:role/RedshiftCopyUnload' csv;"
            )

            # Retrieve the contents of the table
            cursor.execute("select * from motogp")
            print(cursor.fetchall())

    print(df.head())


@flow()
def etl_s3_to_redshift():
    path = extract_from_s3()
    df = transform(path=path)
    write_to_redshift(df=df)


if __name__ == "__main__":
    etl_s3_to_redshift()
