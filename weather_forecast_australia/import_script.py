import sqlite3
import pandas as pd

# Read CSV file
df = pd.read_csv("6f4e1ad2-040d-41a2-8f41-afaf9bd61cd1.csv")

# Connect to SQLite database (file will be created if it doesn't exist)
conn = sqlite3.connect("orange_juice_data.db")

# Write data to a table
df.to_sql("juice_prices", conn, if_exists="replace", index=False)

# Close the connection
conn.close()
