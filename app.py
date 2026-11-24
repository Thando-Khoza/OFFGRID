
import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from data_import import import_energy_data
from data_cleaning import clean_energy_data
from database import save_energy_data, get_energy_data
from analytics import calculate_energy_metrics


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="OFFGRID | Energy Management",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("⚡ OFFGRID")
st.subheader("Energy Management & Analytics Platform")

st.write(
    "Monitor electricity consumption, solar generation, "
    "grid dependency and energy costs."
)

st.divider()


# ==========================================
# DATA IMPORT AND DATABASE INTEGRATION
# ==========================================

@st.cache_data
def load_energy_data():

    raw_data = import_energy_data()

    cleaned_data = clean_energy_data(raw_data)

    save_energy_data(cleaned_data)

    stored_data = get_energy_data()

    stored_data["date"] = pd.to_datetime(
        stored_data["date"]
    )

    return stored_data


try:

    data = load_energy_data()

    if data.empty:
        st.warning("No energy records are available.")
        st.stop()

except Exception as error:

    st.error(f"Unable to load energy data: {error}")
    st.stop()


# ==========================================
# SIDEBAR DASHBOARD CONTROLS
# ==========================================

st.sidebar.title("Dashboard Controls")

st.sidebar.subheader("Date Filter")

minimum_date = data["date"].min().date()
maximum_date = data["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(minimum_date, maximum_date),
    min_value=minimum_date,
    max_value=maximum_date
)

if isinstance(selected_dates, (tuple, list)):

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        filtered_data = data[
            (data["date"].dt.date >= start_date)
            & (data["date"].dt.date <= end_date)
        ]

    else:

        filtered_data = data[
            data["date"].dt.date == selected_dates[0]
        ]

else:

    filtered_data = data[
        data["date"].dt.date == selected_dates
    ]


if filtered_data.empty:

    st.warning("No records found for the selected dates.")
    st.stop()


# ==========================================
# ENERGY ANALYTICS
# ==========================================

metrics = calculate_energy_metrics(filtered_data)


# ==========================================
# ENERGY OVERVIEW
# ==========================================

st.header("Energy Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Consumption",
    f"{metrics['total_consumption']:.2f} kWh"
)

col2.metric(
    "Solar Generation",
    f"{metrics['total_solar']:.2f} kWh"
)

col3.metric(
    "Grid Imports",
    f"{metrics['total_grid_import']:.2f} kWh"
)

col4.metric(
    "Solar Contribution",
    f"{metrics['solar_contribution']:.2f}%"
)


# ==========================================
# ELECTRICITY COSTS
# ==========================================

st.header("Electricity Costs")

cost_col1, cost_col2 = st.columns(2)

cost_col1.metric(
    "Grid Electricity Cost",
    f"R{metrics['total_electricity_cost']:.2f}"
)

cost_col2.metric(
    "Estimated Solar Value",
    f"R{metrics['estimated_solar_savings']:.2f}"
)

st.divider()


# ==========================================
# CONSUMPTION ANALYSIS
# ==========================================

st.header("Energy Consumption Trends")

consumption_chart = px.line(
    filtered_data,
    x="date",
    y="consumption_kwh",
    title="Daily Electricity Consumption",
    markers=True,
    labels={
        "date": "Date",
        "consumption_kwh": "Consumption (kWh)"
    }
)

st.plotly_chart(
    consumption_chart,
    use_container_width=True
)


# ==========================================
# SOLAR PERFORMANCE
# ==========================================

st.header("Solar Performance")

solar_chart = px.bar(
    filtered_data,
    x="date",
    y="solar_kwh",
    title="Daily Solar Generation",
    labels={
        "date": "Date",
        "solar_kwh": "Solar Generation (kWh)"
    }
)

st.plotly_chart(
    solar_chart,
    use_container_width=True
)


# ==========================================
# GRID PERFORMANCE
# ==========================================

st.header("Grid Performance")

grid_chart = px.bar(
    filtered_data,
    x="date",
    y=[
        "grid_import_kwh",
        "grid_export_kwh"
    ],
    title="Grid Imports vs Exports",
    barmode="group",
    labels={
        "date": "Date",
        "value": "Energy (kWh)",
        "variable": "Grid Activity"
    }
)

st.plotly_chart(
    grid_chart,
    use_container_width=True
)


# ==========================================
# BATTERY PERFORMANCE
# ==========================================

st.header("Battery Performance")

battery_chart = px.line(
    filtered_data,
    x="date",
    y=[
        "battery_charge_kwh",
        "battery_discharge_kwh"
    ],
    title="Battery Charging vs Discharging",
    markers=True,
    labels={
        "date": "Date",
        "value": "Energy (kWh)",
        "variable": "Battery Activity"
    }
)

st.plotly_chart(
    battery_chart,
    use_container_width=True
)


# ==========================================
# ENERGY RECORDS
# ==========================================

st.header("Energy Records")

st.dataframe(
    filtered_data,
    use_container_width=True,
    hide_index=True
)


# ==========================================
# CSV EXPORT
# ==========================================

st.header("Export Energy Data")

csv_data = filtered_data.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Energy Records (CSV)",
    data=csv_data,
    file_name="offgrid_energy_report.csv",
    mime="text/csv"
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "OFFGRID | Energy Management & Analytics Platform"
)

st.caption(
    "Built with Python, Streamlit, Pandas, SQLite and Plotly."
)
