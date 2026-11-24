from datetime import datetime


def generate_energy_report(metrics):

    report = f"""
========================================
             OFFGRID ENERGY REPORT
========================================

Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

ENERGY CONSUMPTION
----------------------------------------
Total Consumption: {metrics['total_consumption']} kWh
Average Daily Consumption: {metrics['average_consumption']} kWh

SOLAR PERFORMANCE
----------------------------------------
Total Solar Generation: {metrics['total_solar']} kWh
Solar Contribution: {metrics['solar_contribution']}%

GRID PERFORMANCE
----------------------------------------
Grid Electricity Imported: {metrics['total_grid_import']} kWh
Grid Electricity Exported: {metrics['total_grid_export']} kWh

ELECTRICITY COSTS
----------------------------------------
Total Electricity Cost: R{metrics['total_electricity_cost']}
Estimated Solar Value: R{metrics['estimated_solar_savings']}

========================================
             END OF REPORT
========================================
"""

    return report


if __name__ == "__main__":
    from data_import import import_energy_data
    from data_cleaning import clean_energy_data
    from analytics import calculate_energy_metrics

    energy_data = import_energy_data()
    cleaned_data = clean_energy_data(energy_data)

    metrics = calculate_energy_metrics(cleaned_data)

    report = generate_energy_report(metrics)

    print(report)