from sqlalchemy import create_engine, text

# Replace with your actual password
engine = create_engine('postgresql://taxi_analyst:0000@localhost:5432/nyc_taxi_db')

try:
    with engine.connect() as conn:
        # Wrap raw SQL in text()
        result = conn.execute(text("SELECT 1"))
        print("Connection successful! Test query returned:", result.scalar())
except Exception as e:
    print("Connection failed:", str(e))
