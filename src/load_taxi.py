import pyarrow.parquet as pq
import pandas as pd
from sqlalchemy import create_engine
import os

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARQUET_FILE = os.path.join(BASE_DIR, 'data/raw/yellow_tripdata_2025-01.parquet')
BATCH_SIZE = 100000

# Change '0000' to your actual database password if different
engine = create_engine('postgresql://taxi_analyst:0000@localhost:5432/nyc_taxi_db')

print("🚀 Starting chunked load from Parquet to PostgreSQL...")

if not os.path.exists(PARQUET_FILE):
    print(f"❌ Error: Parquet file not found at:\n{PARQUET_FILE}")
    exit(1)

parquet_reader = pq.ParquetFile(PARQUET_FILE)

for i, batch in enumerate(parquet_reader.iter_batches(batch_size=BATCH_SIZE)):
    print(f"Processing batch {i+1} ({len(batch):,} rows)...")
    df_chunk = batch.to_pandas()
    mode = 'replace' if i == 0 else 'append'
    df_chunk.to_sql('yellow_trips_2025_01', engine, if_exists=mode, index=False)
    del df_chunk, batch  # Free memory

print("✅ Load completed successfully! Table 'yellow_trips_2025_01' is ready.")
