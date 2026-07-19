"""
Smart Fuel Station Intelligence System
Generate Pumps Dataset

Author: Sumeet Chandekar
"""

import random
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_FOLDER = BASE_DIR / "dataset"

# --------------------------------------------------
# Read Stations Dataset
# --------------------------------------------------

stations = pd.read_csv(DATASET_FOLDER / "stations.csv")

# --------------------------------------------------
# Constants
# --------------------------------------------------

FUEL_TYPES = [
    "Petrol",
    "Diesel",
    "Premium Petrol",
    "CNG"
]

MANUFACTURERS = [
    "Gilbarco",
    "Wayne",
    "Tatsuno",
    "Tokheim"
]

STATUS = [
    "Active",
    "Maintenance"
]

# --------------------------------------------------
# Generate Pumps
# --------------------------------------------------

pumps = []

pump_counter = 1

for _, station in stations.iterrows():

    station_id = station["Station_ID"]

    # Every station will have 4–8 pumps
    number_of_pumps = random.randint(4, 8)

    for pump_no in range(1, number_of_pumps + 1):

        pump_id = f"P{pump_counter:06d}"

        fuel_type = random.choice(FUEL_TYPES)

        manufacturer = random.choice(MANUFACTURERS)

        install_year = random.randint(2016, 2025)

        status = random.choices(
            STATUS,
            weights=[90, 10],   # 90% Active, 10% Maintenance
            k=1
        )[0]

        pumps.append({

            "Pump_ID": pump_id,

            "Station_ID": station_id,

            "Pump_Number": pump_no,

            "Fuel_Type": fuel_type,

            "Manufacturer": manufacturer,

            "Installation_Year": install_year,

            "Status": status

        })

        pump_counter += 1

# --------------------------------------------------
# Convert to DataFrame
# --------------------------------------------------

pump_df = pd.DataFrame(pumps)

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

output_file = DATASET_FOLDER / "pumps.csv"

pump_df.to_csv(output_file, index=False)

# --------------------------------------------------
# Output
# --------------------------------------------------

print(pump_df.head())

print("\n-------------------------------------")
print("Pumps Generated Successfully")
print("-------------------------------------")

print(f"Total Pumps Generated : {len(pump_df)}")
print(f"CSV Saved At          : {output_file}")
