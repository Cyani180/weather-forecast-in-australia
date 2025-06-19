import sqlite3
import pandas as pd

# Load CSV file
df = pd.read_csv('data/weatherAUS_clean.csv')

# Connect to the SQLite database
conn = sqlite3.connect('weather_forecast_data.db')
cursor = conn.cursor()

# Create table and insert data (automatically creates columns)
df.to_sql('weather_clean', conn, if_exists='replace', index=False)

print("✅ Daten erfolgreich in die SQLite-Datenbank importiert.")

conn.close()
