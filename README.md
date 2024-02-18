# Docker-SQL

### Introduction
This is a simple pipeline with NYC's Taxi data. The pipeline will ingest data from a CSV file, basic data integrity checks, and load it into Postgres DB. Then, some data aggregations are done in pgAdmin. The application is containerized using Docker.

### About the pipeline

1. The dataset is downloaded in a parquet format from this link - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page.

2. We spin up a Jupyter Notebook and using pandas, we convert the format from parquet to CSV. After this, we study the data and do basic data quality checks such as dropping unwanted columns, and schema studying.

3. For pushing the data to our Postgres DB, we create a connection using SQLAlchemy, iterate through chunks of data and push it with the help of a while loop.

4. We also download one more Taxi Zone Map dataset from the same link above for manipulation purposes and push it to the same Postgres DB.

5. In pgAdmin, we do JOINs and GroupBys in SQL for retrieving our desired information.

### Dockerized
The main services that we have used in building this pipeline were Postgres and pgAdmin. I have created a Docker Compose file with the 3 images for spinning up the respective services.
- Postgres container exposes port 5432
- pgAdmin container exposes port 8080
- Jupyter container exposes port 8888  

The ingestion script is written in Jupyter Notebook and even though it's not necessary, I have still created a Jupyter Notebook image inside the Compose file that will run it in 8888.

### Information about the files
1. Dockerfile - This file is not used that much as we are using Docker Compose mostly for our services as I was not using any particular version.
2. docker-compose.yaml - Instructions to run the services.
3. taxi+_zone_lookup.csv - This is the Taxi Zone Map dataset file downloaded from the link I have pasted in the above section.
4. test.py - This is just a test file. Nothing's here.
5. upload-data-to-postgres.ipynb - Pipeline script to ingest and push data to DB.
6. yellow_tripdata_2023-01.parquet - This is the parquet file downloaded from the link.

Trivial
- The converted CSV file is too big to be pushed here to this repository.
- This project is part of the DE ZoomCamp 2024.

  
