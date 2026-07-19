"""
Smart Fuel Station Intelligence System
Generate Transactions

Author: Sumeet Chandekar
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from config import DATASET_FOLDER, NUM_TRANSACTIONS
from constants import (
    PAYMENT_MODES,
    CONTAINER_TYPES
)

# -----------------------------------
# Load Dataset
# -----------------------------------

stations = pd.read_csv(DATASET_FOLDER / "stations.csv")
pumps = pd.read_csv(DATASET_FOLDER / "pumps.csv")
employees = pd.read_csv(DATASET_FOLDER / "employees.csv")
customers = pd.read_csv(DATASET_FOLDER / "customers.csv")
vehicles = pd.read_csv(DATASET_FOLDER / "vehicles.csv")

transactions = []

# -----------------------------------
# Fuel Prices
# -----------------------------------

fuel_price = {
    "Petrol": 111.21,
    "Diesel": 97.83,
    "Premium Petrol": 118.00,
    "CNG": 96.50
}

# -----------------------------------
# Fuel Quantity
# -----------------------------------

fuel_quantity = {
    "Bike": (2, 12),
    "Car": (15, 45),
    "SUV": (20, 60),
    "Truck": (100, 350),
    "Bus": (120, 450),
    "Auto": (3, 10),
    "Tractor": (20, 80)
}

# -----------------------------------
# Weather
# -----------------------------------

weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Foggy"
]

# -----------------------------------
# Random Date Time
# -----------------------------------

def random_datetime():

    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    seconds = random.randint(
        0,
        int((end - start).total_seconds())
    )

    return start + timedelta(seconds=seconds)

# -----------------------------------
# Customer -> Vehicles
# -----------------------------------

customer_vehicle_map = {}

for _, row in vehicles.iterrows():

    customer_id = row["Customer_ID"]

    if customer_id not in customer_vehicle_map:
        customer_vehicle_map[customer_id] = []

    customer_vehicle_map[customer_id].append(row.to_dict())

# -----------------------------------
# Station -> Pumps
# -----------------------------------

station_pump_map = {}

for _, row in pumps.iterrows():

    station_id = row["Station_ID"]

    if station_id not in station_pump_map:
        station_pump_map[station_id] = []

    station_pump_map[station_id].append(row.to_dict())

# -----------------------------------
# Station -> Employees
# -----------------------------------

station_employee_map = {}

for _, row in employees.iterrows():

    station_id = row["Station_ID"]

    if station_id not in station_employee_map:
        station_employee_map[station_id] = []

    station_employee_map[station_id].append(row.to_dict())
# -----------------------------------
# Generate Transactions
# -----------------------------------

for transaction_no in range(1, NUM_TRANSACTIONS + 1):

    transaction_id = f"TRX{transaction_no:07d}"

    customer = customers.sample(1).iloc[0]
    customer_id = customer["Customer_ID"]

    transaction_type = random.choices(
        ["Vehicle", "Container"],
        weights=[97, 3]
    )[0]

    vehicle_id = None
    vehicle_type = None
    container_type = None
    fuel_type = None

    # -----------------------------
    # Vehicle Transaction
    # -----------------------------

    if transaction_type == "Vehicle":

        if customer_id not in customer_vehicle_map:
            continue

        vehicle = random.choice(
            customer_vehicle_map[customer_id]
        )

        vehicle_id = vehicle["Vehicle_ID"]
        vehicle_type = vehicle["Vehicle_Type"]
        fuel_type = vehicle["Fuel_Type"]

    # -----------------------------
    # Container Transaction
    # -----------------------------

    else:

        container_type = random.choice(CONTAINER_TYPES)

        fuel_type = random.choice([
            "Petrol",
            "Diesel",
            "CNG"
        ])

    # -----------------------------
    # Station
    # -----------------------------

    station = stations.sample(1).iloc[0]

    station_id = station["Station_ID"]

    pump = random.choice(
        station_pump_map[station_id]
    )

    pump_id = pump["Pump_ID"]

    employee = random.choice(
        station_employee_map[station_id]
    )

    employee_id = employee["Employee_ID"]

    # -----------------------------
    # Date & Time
    # -----------------------------

    dt = random_datetime()

    transaction_date = dt.date()

    transaction_time = dt.strftime("%H:%M:%S")

    # -----------------------------
    # Fuel Quantity
    # -----------------------------

    if transaction_type == "Vehicle":

        min_qty, max_qty = fuel_quantity[vehicle_type]

        quantity = round(
            random.uniform(min_qty, max_qty),
            2
        )

    else:

        quantity = round(
            random.uniform(2, 50),
            2
        )

    # -----------------------------
    # Amount
    # -----------------------------

    price_per_litre = fuel_price[fuel_type]

    total_amount = round(
        quantity * price_per_litre,
        2
    )

    payment_mode = random.choices(
        PAYMENT_MODES,
        weights=[50, 15, 20, 10, 5]
    )[0]

    loyalty_points = int(total_amount // 100)

    transaction_status = random.choices(
        ["Success", "Failed"],
        weights=[99, 1]
    )[0]

    weather = random.choice(
        weather_conditions
    )
    # -----------------------------
    # Create Transaction Record
    # -----------------------------

    transaction = {

        "Transaction_ID": transaction_id,

        "Transaction_Date": transaction_date,

        "Transaction_Time": transaction_time,

        "Station_ID": station_id,

        "Pump_ID": pump_id,

        "Employee_ID": employee_id,

        "Customer_ID": customer_id,

        "Transaction_Type": transaction_type,

        "Vehicle_ID": vehicle_id,

        "Container_Type": container_type,

        "Fuel_Type": fuel_type,

        "Quantity_Litres": quantity,

        "Price_Per_Litre": price_per_litre,

        "Total_Amount": total_amount,

        "Payment_Mode": payment_mode,

        "Loyalty_Points": loyalty_points,

        "Transaction_Status": transaction_status,

        "Weather": weather

    }

    # -----------------------------
    # Add to List
    # -----------------------------

    transactions.append(transaction)
# -----------------------------------
# Save Transactions
# -----------------------------------

df = pd.DataFrame(transactions)

df = df.sort_values(
    by=["Transaction_Date", "Transaction_Time"]
)

df.reset_index(
    drop=True,
    inplace=True
)

df.to_csv(
    DATASET_FOLDER / "transactions.csv",
    index=False
)

print(df.head())

print()

print(f"Total Transactions Generated: {len(df)}")

print()

print("Transactions Generated Successfully.")