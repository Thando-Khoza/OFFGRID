import pandas as pd


def calculate_energy_metrics(data):

    if data.empty:
        raise ValueError("No energy data available for analysis.")

    total_consumption = data["consumption_kwh"].sum()
    total_solar = data["solar_kwh"].sum()
    total_grid_import = data["grid_import_kwh"].sum()
    total_grid_export = data["grid_export_kwh"].sum()

    average_consumption = data["consumption_kwh"].mean()

    solar_contribution = (
        (total_solar / total_consumption) * 100
        if total_consumption > 0 else 0
    )

    total_electricity_cost = (
        data["grid_import_kwh"] * data["electricity_rate"]
    ).sum()

    estimated_solar_savings = (
        data["solar_kwh"] * data["electricity_rate"]
    ).sum()

    return {
        "total_consumption": round(total_consumption, 2),
        "total_solar": round(total_solar, 2),
        "total_grid_import": round(total_grid_import, 2),
        "total_grid_export": round(total_grid_export, 2),
        "average_consumption": round(average_consumption, 2),
        "solar_contribution": round(solar_contribution, 2),
        "total_electricity_cost": round(total_electricity_cost, 2),
        "estimated_solar_savings": round(estimated_solar_savings, 2)
    }


if __name__ == "__main__":
    from data_import import import_energy_data
    from data_cleaning import clean_energy_data

    energy_data = import_energy_data()
    cleaned_data = clean_energy_data(energy_data)

    metrics = calculate_energy_metrics(cleaned_data)

    print("\nOFFGRID ENERGY ANALYTICS")
    print("-----------------------")

    for metric, value in metrics.items():
        print(f"{metric.replace('_', ' ').title()}: {value}")