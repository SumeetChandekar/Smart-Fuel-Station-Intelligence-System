"""
Smart Fuel Station Intelligence System
Generate Fuel Stations

Author: Sumeet Chandekar
"""

import random
import pandas as pd

from config import NUM_STATIONS
from constants import CITIES

# -----------------------------
# Localities by City
# -----------------------------

CITY_LOCALITIES = {
    "Pune": [
        "Baner","Wakad","Hinjawadi","Kharadi","Hadapsar",
        "Kothrud","Viman Nagar","Magarpatta","Nigdi","Pimple Saudagar"
    ],

    "Mumbai": [
        "Andheri","Bandra","Powai","Borivali","Chembur",
        "Kurla","Dadar","Malad","Colaba","Goregaon"
    ],

    "Navi Mumbai": [
        "Vashi","Nerul","Belapur","Kharghar","Airoli",
        "Ghansoli","Panvel"
    ]
}
stations = []

for i in range(1, NUM_STATIONS + 1):

    station_id = f"ST{i:04d}"

    city = random.choice(CITIES)

    if city in CITY_LOCALITIES:
        locality = random.choice(CITY_LOCALITIES[city])
    else:
        locality = city

    station_name = f"FuelSense {locality}"

    capacity = random.choice([
        40000,
        50000,
        60000,
        70000,
        80000
    ])

    stations.append({

        "Station_ID": station_id,

        "Station_Name": station_name,

        "City": city,

        "Storage_Capacity_Litres": capacity

    })

df =pd.DataFrame(stations)

df.to_csv("../dataset/stations.csv", index=False)

print(df.head())

print("\nStations Generated Successfully.")  
