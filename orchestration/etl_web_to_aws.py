import os
from pathlib import Path

import pandas as pd
import pycountry
from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect_aws import S3Bucket


@task(name="fetch", retries=3, cache_key_fn=task_input_hash)
def read_data(data_path: str):
    """Read the data"""
    df = pd.read_csv(data_path)
    print(df.head())
    return df


@task(name="clean", log_prints=True)
def clean(df: pd.DataFrame):
    """Convert country codes to country name"""
    df = df.dropna(axis=0)
    df["country"] = df.country.apply(lambda x: pycountry.countries.get(alpha_2=x).name)
    df["season"] = pd.to_datetime(df["season"], format="%Y")
    print(df.head())
    return df


@task(name="write_to_local")
def write_local(df: pd.DataFrame) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path("../data-extraction/data/ref/")

    df.to_parquet(os.path.join(path, "motogp.parquet"), compression="gzip")
    return path


@task(name="write_to_s3")
def write_s3(path: Path):
    """Upload local parquet file to S3"""
    s3_bucket = S3Bucket.load("moto-gp")

    s3_bucket.upload_from_folder(from_folder=path, to_folder="data")
    return


@flow()
def etl_web_to_aws() -> None:
    """The main ETL function"""
    dataset_dir = "../data-extraction/data/raw/motogp.csv"

    df = read_data(dataset_dir)
    df_clean = clean(df)
    path = write_local(df_clean)
    write_s3(path)


if __name__ == "__main__":
    etl_web_to_aws()
