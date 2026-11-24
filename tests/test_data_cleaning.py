
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

from data_cleaning import clean_energy_data


@pytest.fixture
def sample_data():

    return pd.DataFrame({
        "date": [
            "2026-10-01",
            "2026-10-02",
            "2026-10-03"
        ],
        "consumption_kwh": [24.5, 22.0, 28.0],
        "solar_kwh": [18.0, 20.0, 15.0],
        "grid_import_kwh": [12.0, 8.0, 17.0],
        "grid_export_kwh": [5.5, 6.0, 2.0],
        "battery_charge_kwh": [8.0, 9.0, 6.0],
        "battery_discharge_kwh": [6.0, 5.0, 8.0],
        "electricity_rate": [3.20, 3.20, 3.20]
    })


def test_clean_valid_data(sample_data):

    cleaned_data = clean_energy_data(sample_data)

    assert len(cleaned_data) == 3
    assert cleaned_data.isnull().sum().sum() == 0


def test_remove_duplicate_records(sample_data):

    duplicated_data = pd.concat(
        [sample_data, sample_data.iloc[[0]]],
        ignore_index=True
    )

    cleaned_data = clean_energy_data(duplicated_data)

    assert len(cleaned_data) == 3


def test_remove_negative_values(sample_data):

    sample_data.loc[0, "consumption_kwh"] = -10

    cleaned_data = clean_energy_data(sample_data)

    assert len(cleaned_data) == 2
    assert (cleaned_data["consumption_kwh"] >= 0).all()


def test_remove_invalid_dates(sample_data):

    sample_data.loc[0, "date"] = "invalid-date"

    cleaned_data = clean_energy_data(sample_data)

    assert len(cleaned_data) == 2


def test_missing_columns_raise_error(sample_data):

    sample_data = sample_data.drop(
        columns=["solar_kwh"]
    )

    with pytest.raises(ValueError):

        clean_energy_data(sample_data)
