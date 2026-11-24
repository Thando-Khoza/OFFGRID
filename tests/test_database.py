
import sys
import sqlite3
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

import database


@pytest.fixture
def temporary_database(tmp_path, monkeypatch):

    test_database_path = tmp_path / "test_offgrid.db"

    monkeypatch.setattr(
        database,
        "DATABASE_PATH",
        test_database_path
    )

    return test_database_path


@pytest.fixture
def sample_data():

    return pd.DataFrame({
        "date": pd.to_datetime([
            "2026-10-01",
            "2026-10-02"
        ]),
        "consumption_kwh": [24.5, 22.0],
        "solar_kwh": [18.0, 20.0],
        "grid_import_kwh": [12.0, 8.0],
        "grid_export_kwh": [5.5, 6.0],
        "battery_charge_kwh": [8.0, 9.0],
        "battery_discharge_kwh": [6.0, 5.0],
        "electricity_rate": [3.20, 3.20]
    })


def test_create_database(temporary_database):

    database.create_database()

    assert temporary_database.exists()


def test_save_and_retrieve_energy_data(
    temporary_database,
    sample_data
):

    database.save_energy_data(sample_data)

    retrieved_data = database.get_energy_data()

    assert len(retrieved_data) == 2
    assert retrieved_data.iloc[0]["consumption_kwh"] == 24.5


def test_update_existing_records(
    temporary_database,
    sample_data
):

    database.save_energy_data(sample_data)

    updated_data = sample_data.copy()

    updated_data.loc[0, "consumption_kwh"] = 30.0

    database.save_energy_data(updated_data)

    retrieved_data = database.get_energy_data()

    assert len(retrieved_data) == 2
    assert retrieved_data.iloc[0]["consumption_kwh"] == 30.0

