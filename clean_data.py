import pandas as pd
import os

def clean_csv(input_path, output_path):
    # CSV laden
    df = pd.read_csv(input_path)

    # Nur numerische Spalten behalten (int, float)
    df_numeric = df.select_dtypes(include=['number'])

    # Alle Zeilen mit NaN entfernen
    df_clean = df_numeric.dropna()

    # Gesäuberte CSV speichern
    df_clean.to_csv(output_path, index=False)
    print(f"Gesäuberte CSV gespeichert unter {output_path}")

if __name__ == "__main__":
    input_csv = "weatherAUS.csv"  # deine originale CSV
    output_csv = os.path.join("data", "weatherAUS_clean.csv")  # Ziel im data Ordner

    # Ordner data erstellen, falls nicht vorhanden
    os.makedirs("data", exist_ok=True)

    clean_csv(input_csv, output_csv)
