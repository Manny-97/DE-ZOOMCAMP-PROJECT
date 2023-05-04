FROM python:3.9

RUN apt-get install wget
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY  ingest.py ingest.py
COPY  scraper.py scraper.py

ENTRYPOINT [ "python", "ingest.py" ]
