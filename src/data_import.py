
import pandas as pd
from pathlib import Path

from database import save_energy_data


DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "energy_data.csv"
)


def import_energy_data():

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Energy CSV file was not found."
        )

    data = pd.read_csv(DATA_PATH)

    print("CSV file imported successfully!")
    print(f"Total records: {len(data)}")

    return data


def import_and_save_energy_data(cleaned_data):

    save_energy_data(cleaned_data)


if __name__ == "__main__":

    energy_data = import_energy_data()

    print("\nENERGY DATA PREVIEW")
    print("-------------------")
    print(energy_data.head())
