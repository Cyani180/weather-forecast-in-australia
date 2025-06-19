import sqlite3
import pandas as pd

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("weather_forecast_data.db")
query = "SELECT * FROM weather"
df = pd.read_sql_query(query, conn)

# Einfache Analyse
report_lines = []

report_lines.append(f"Gesamtanzahl der Datensätze: {len(df)}")
report_lines.append(f"Spalten: {', '.join(df.columns)}")
report_lines.append(f"\nNaN-Werte pro Spalte:\n{df.isnull().sum()}")

# Report schreiben
with open("metrics/analysis_report.txt", "w") as f:
    f.write("\n".join(report_lines))

conn.close()
