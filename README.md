# Palisades Fire Data

This repository contains structured data and code related to the Palisades Fire incident, sourced from the [Palisades Fire Updates](https://www.fire.ca.gov/incidents/2025/1/7/palisades-fire/updates) page on the CAL FIRE website.

## Overview

The data was collected using web scraping techniques and includes detailed updates about the Palisades Fire incident from **January 7 to February 10, 2025**. The repository provides both the raw and cleaned datasets, as well as a Python script for data cleaning and extraction.

## Data Contents

The cleaned dataset includes the following variables:
- Incident Name
- Page DateTime (timestamp of the update page)
- Start DateTime (precise ignition timestamp)
- Incident Status
- Location
- Type (e.g., Wildfire)
- Cause
- Counties
- Acres Burned
- Containment (%)
- Structures Threatened
- Structures Destroyed
- Structures Damaged
- Civilian Injuries
- Firefighter Injuries
- Civilian Fatalities
- Total Personnel
- Engines
- Water Tenders
- Hand Crews
- Other Resources
- Administration Unit
- Unified Command Agency(s)

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/palisades-fire-data.git
    ```
2. Access the data files in the repository:
    - `calfire_updates_raw_data.csv`: Raw scraped data
    - `calfire_updates_cleaned.csv`: Cleaned, structured data
    - `data_cleaning.py`: Python script for data cleaning
3. To generate the cleaned data from raw data, run:
    ```bash
    python data_cleaning.py
    ```

## Disclaimer

The data is sourced directly from the CAL FIRE website. Ensure proper attribution if used in any publication or project.