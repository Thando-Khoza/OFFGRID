import pandas as pd


def clean_energy_data(data):
    required_columns = [
        "date",
        "consumption_kwh",
        "solar_kwh",
        "grid_import_kwh",
        "grid_export_kwh",
        "battery_charge_kwh",
        "battery_discharge_kwh",
        "electricity_rate"
    ]

    # Check that all required columns exist
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Work with a copy of the original dataset
    data = data.copy()

    # Remove duplicate records
    data = data.drop_duplicates()

    # Convert date values
    data["date"] = pd.to_datetime(data["date"], errors="coerce")

    # Convert energy and rate columns into numbers
    numeric_columns = required_columns[1:]

    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Remove rows containing missing or invalid values
    data = data.dropna(subset=required_columns)

    # Check for negative values
    for column in numeric_columns:
        data = data[data[column] >= 0]

    # Reset row numbering
    data = data.reset_index(drop=True)

    return data


if __name__ == "__main__":
    from data_import import import_energy_data

    energy_data = import_energy_data()
    cleaned_data = clean_energy_data(energy_data)

    print("\nDATA CLEANING REPORT")
    print("--------------------")
    print(f"Original records: {len(energy_data)}")
    print(f"Clean records: {len(cleaned_data)}")
    print(f"Removed records: {len(energy_data) - len(cleaned_data)}")

    print("\nCLEANED DATA PREVIEW")
    print("--------------------")
    print(cleaned_data.head())