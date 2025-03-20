# Ad Campaign Data Analysis

This project is a tool for validating and analyzing ad campaign data, designed to assist in managing and evaluating marketing campaigns. It includes features for data validation, exploratory reporting, and KPI visualization.

## Features

1. **Data Validation**: Uses `pydantic` to validate input data against a defined data contract.
2. **Exploratory Analysis**: Generates an initial exploratory report using `ydata_profiling`.
3. **Interactive Dashboard**: A dashboard built with `Streamlit` for KPI visualization and interactive data analysis.

## Project Structure

- **main.py**: Main script to generate the exploratory report.
- **validador.py**: Contains the `Anuncio` model for validating input data.
- **app.py**: Streamlit application for validating CSV files.
- **dashboard.py**: Interactive dashboard for analyzing ad campaign KPIs.