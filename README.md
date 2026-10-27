# NYC Yellow Taxi Data Pipeline (January 2025)

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Parquet](https://img.shields.io/badge/Parquet-PyArrow-green.svg)

## Overview

A Python pipeline that loads the NYC Yellow Taxi trip records for January 2025 (3,475,226 trips) from a Parquet file into PostgreSQL.

**Key Highlights:**
- Reads the Parquet file in 100,000-row batches with PyArrow, so the full dataset is never held in memory
- Writes each batch to PostgreSQL with SQLAlchemy and pandas
- Includes a database connection test and a plotting test script

## Dataset

- **Source**: New York City Taxi & Limousine Commission (TLC)
- **Period**: January 2025
- **Records**: 3,475,226 trips
- **Format**: Parquet (`yellow_tripdata_2025-01.parquet`)
- **Fields include**: pickup/dropoff times, trip distance, pickup/dropoff zone IDs, fare, tip, tolls, total amount, congestion surcharge, and airport fee

[Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

## Project Structure

```bash
NYC-Taxi-Analysis/
├── data/raw/              # place yellow_tripdata_2025-01.parquet here
├── src/
│   ├── load_taxi.py      # Load Parquet → PostgreSQL
│   ├── test_conn.py      # DB connection test
│   └── test_plot.py      # Plotting test
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a PostgreSQL database named `nyc_taxi_db` and a user with access to it
3. Set your database credentials in `src/load_taxi.py` (never commit real passwords)
4. Download the January 2025 Yellow Taxi Parquet file from the TLC into `data/raw/`
5. Run `python src/load_taxi.py`

The loader writes to a table named `yellow_trips_2025_01`. The first batch **replaces** the table if it exists, so re-running starts from scratch.

## Status

- **Done:** batched loading from Parquet into PostgreSQL
- **Next:** SQL analysis (aggregations by hour and pickup zone), saved queries, and charts
