import os

import pyarrow.parquet as pq
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARQUET_FILE = os.path.join(BASE_DIR, 'data/raw/yellow_tripdata_2025-01.parquet')
BATCH_SIZE = 100000

engine = create_engine(
    URL.create(
        "postgresql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME", "nyc_taxi_db"),
    )
)

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
