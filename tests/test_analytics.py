
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

from analytics import calculate_energy_metrics


@pytest.fixture
def sample_data():

    return pd.DataFrame({
        "date": ["2026-10-01", "2026-10-02"],
        "consumption_kwh": [20.0, 30.0],
        "solar_kwh": [10.0, 20.0],
        "grid_import_kwh": [12.0, 8.0],
        "grid_export_kwh": [3.0, 5.0],
        "battery_charge_kwh": [5.0, 7.0],
        "battery_discharge_kwh": [4.0, 6.0],
        "electricity_rate": [3.20, 3.20]
    })


def test_total_energy_consumption(sample_data):

    metrics = calculate_energy_metrics(sample_data)

    assert metrics["total_consumption"] == 50.0


def test_total_solar_generation(sample_data):

    metrics = calculate_energy_metrics(sample_data)

    assert metrics["total_solar"] == 30.0


def test_total_grid_import(sample_data):

    metrics = calculate_energy_metrics(sample_data)

    assert metrics["total_grid_import"] == 20.0


def test_average_consumption(sample_data):

    metrics = calculate_energy_metrics(sample_data)

    assert metrics["average_consumption"] == 25.0


def test_electricity_cost(sample_data):

    metrics = calculate_energy_metrics(sample_data)

    assert metrics["total_electricity_cost"] == 64.0


def test_empty_data_raises_error():

    empty_data = pd.DataFrame()

    with pytest.raises(ValueError):

        calculate_energy_metrics(empty_data)
