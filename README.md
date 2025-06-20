# weather-forecast-in-australia

Using the SQLite Database
This project includes a preprocessed SQLite database (weather_forecast_data.db) 
with cleaned weather data to make collaboration easier.

How to use the database

1. Clone the repository:

git clone https://github.com/Cyani180/weather-forecast-in-australia.git
cd weather-forecast-in-australia


2. Crate and activate avirtual environment:

python3 -m venv venv
source venv/bin/activate


3. Install required dependencies:

pip install -r requirements.txt


4. (Optional) Re-import the cleaned CSV into the databse:
If you want to regenerate the databse from the cleaned CSV file, run:

python import_clean_data.py


5. Access the databse in your Python scripts:
You can connect to weather_forecast_data.db using SQLite3 or any database client.

Example in Python:

import sqlite3

conn = sqlite3.connect('weather_forecast_data.db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(*) FROM weather_clean')
print(cursor.fetchone())

conn.close()

