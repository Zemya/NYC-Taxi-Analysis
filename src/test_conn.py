import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

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

try:
    with engine.connect() as conn:
        # Wrap raw SQL in text()
        result = conn.execute(text("SELECT 1"))
        print("Connection successful! Test query returned:", result.scalar())
except Exception as e:
    print("Connection failed:", str(e))
