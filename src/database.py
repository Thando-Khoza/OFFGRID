
import sqlite3
import pandas as pd
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).resolve().parent.parent
    / "database"
    / "offgrid.db"
)


def create_database():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS energy_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                consumption_kwh REAL NOT NULL,
                solar_kwh REAL NOT NULL,
                grid_import_kwh REAL NOT NULL,
                grid_export_kwh REAL NOT NULL,
                battery_charge_kwh REAL NOT NULL,
                battery_discharge_kwh REAL NOT NULL,
                electricity_rate REAL NOT NULL
            )
        """)

        connection.execute("""
            CREATE UNIQUE INDEX IF NOT EXISTS idx_energy_records_date
            ON energy_records(date)
        """)

    print("OFFGRID database created successfully!")


def save_energy_data(data):
    create_database()

    records = data.copy()
    records["date"] = records["date"].astype(str)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.executemany("""
            INSERT INTO energy_records (
                date,
                consumption_kwh,
                solar_kwh,
                grid_import_kwh,
                grid_export_kwh,
                battery_charge_kwh,
                battery_discharge_kwh,
                electricity_rate
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(date) DO UPDATE SET
                consumption_kwh = excluded.consumption_kwh,
                solar_kwh = excluded.solar_kwh,
                grid_import_kwh = excluded.grid_import_kwh,
                grid_export_kwh = excluded.grid_export_kwh,
                battery_charge_kwh = excluded.battery_charge_kwh,
                battery_discharge_kwh = excluded.battery_discharge_kwh,
                electricity_rate = excluded.electricity_rate
        """, records.values.tolist())

    print(f"{len(records)} energy records saved successfully!")


def get_energy_data():
    create_database()

    with sqlite3.connect(DATABASE_PATH) as connection:
        data = pd.read_sql_query(
            "SELECT * FROM energy_records ORDER BY date",
            connection
        )

    return data


if __name__ == "__main__":
    create_database()


