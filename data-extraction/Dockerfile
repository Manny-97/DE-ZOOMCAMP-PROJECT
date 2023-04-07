FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY  ingest.py ingest.py

ENTRYPOINT [ "python", "ingest.py" ]