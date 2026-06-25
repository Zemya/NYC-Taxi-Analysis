# NYC Yellow Taxi Trip Data Analysis (January 2025)

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Parquet](https://img.shields.io/badge/Parquet-Efficient-green.svg)

## Overview

Professional **data engineering & analysis** project using real **NYC Yellow Taxi Trip Records** for January 2025 (~3.48 million trips).

**Key Highlights:**
- Efficient handling of large Parquet file using PyArrow
- Chunked loading into PostgreSQL (memory efficient)
- Clean, modular project structure
- Ready for EDA, visualization, and insights

## Dataset

- **Source**: New York City Taxi & Limousine Commission (TLC)
- **Period**: January 2025
- **Records**: ~3.48 million trips
- **Format**: Parquet (`yellow_tripdata_2025-01.parquet`)
- **Special Column**: `cbd_congestion_fee` (new 2025 congestion pricing)

[Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

## Project Structure

```bash
NYtaxi/
├── data/raw/yellow_tripdata_2025-01.parquet
├── src/
│   ├── load_taxi.py      # Load Parquet → PostgreSQL
│   ├── test_conn.py      # DB connection test
│   └── test_plot.py      # Visualization test
├── requirements.txt
├── .gitignore
└── README.md
