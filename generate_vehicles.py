"""
Smart Fuel Station Intelligence System
Generate Vehicles Dataset

Author: Sumeet Chandekar
"""

import random
import string
import pandas as pd

from config import DATASET_FOLDER

customers = pd.read_csv(DATASET_FOLDER / "customers.csv")

vehicles = []

vehicle_no = 1
CAR_BRANDS = [
    "Maruti",
    "Hyundai",
    "Honda",
    "Toyota",
    "Tata",
    "Mahindra",
    "Kia"
]

BIKE_BRANDS = [
    "Hero",
    "Honda",
    "TVS",
    "Bajaj",
    "Yamaha",
    "Royal Enfield"
]

SUV_BRANDS = [
    "Mahindra",
    "Toyota",
    "Hyundai",
    "Tata",
    "MG",
    "Kia"
]

TRUCK_BRANDS = [
    "Tata",
    "Ashok Leyland",
    "Eicher"
]

BUS_BRANDS = [
    "Tata",
    "Ashok Leyland",
    "Volvo"
]

AUTO_BRANDS = [
    "Bajaj",
    "Piaggio",
    "Mahindra"
]

TRACTOR_BRANDS = [
    "Mahindra",
    "Swaraj",
    "Sonalika"
]
def get_brand(vehicle_type):

    if vehicle_type == "Bike":
        return random.choice(BIKE_BRANDS)

    elif vehicle_type == "Car":
        return random.choice(CAR_BRANDS)

    elif vehicle_type == "SUV":
        return random.choice(SUV_BRANDS)

    elif vehicle_type == "Truck":
        return random.choice(TRUCK_BRANDS)

    elif vehicle_type == "Bus":
        return random.choice(BUS_BRANDS)

    elif vehicle_type == "Auto":
        return random.choice(AUTO_BRANDS)

    else:
        return random.choice(TRACTOR_BRANDS)


def get_fuel(vehicle_type):

    if vehicle_type == "Bike":
        return "Petrol"

    elif vehicle_type == "Car":
        return random.choice(["Petrol", "Diesel", "CNG"])

    elif vehicle_type == "SUV":
        return random.choice(["Petrol", "Diesel"])

    elif vehicle_type == "Truck":
        return "Diesel"

    elif vehicle_type == "Bus":
        return random.choice(["Diesel", "CNG"])

    elif vehicle_type == "Auto":
        return random.choice(["Petrol", "CNG"])

    else:
        return "Diesel"


def registration_number():

    rto = random.choice([
        "12",  # Pune
        "14",  # Pimpri-Chinchwad
        "46",  # Navi Mumbai
        "43",  # Mumbai
        "20",  # Nagpur
        "31",  # Nashik
        "11",  # Thane
        "13"   # Solapur
    ])

    letters = "".join(random.choices(string.ascii_uppercase, k=2))

    numbers = random.randint(1000, 9999)

    return f"MH{rto}{letters}{numbers}"
COLORS = [
    "White",
    "Black",
    "Silver",
    "Grey",
    "Blue",
    "Red"
]

for _, customer in customers.iterrows():

    customer_id = customer["Customer_ID"]

    vehicle_count = random.choices(
        [0, 1, 2, 3],
        weights=[5, 55, 30, 10]
    )[0]

    for i in range(vehicle_count):

        vehicle_id = f"VEH{vehicle_no:06d}"

        vehicle_type = random.choice([
            "Bike",
            "Car",
            "SUV",
            "Truck",
            "Bus",
            "Auto",
            "Tractor"
        ])

        brand = get_brand(vehicle_type)

        fuel_type = get_fuel(vehicle_type)

        registration = registration_number()

        year = random.randint(2012, 2025)

        color = random.choice(COLORS)

        vehicles.append({

            "Vehicle_ID": vehicle_id,

            "Customer_ID": customer_id,

            "Registration_Number": registration,

            "Vehicle_Type": vehicle_type,

            "Brand": brand,

            "Fuel_Type": fuel_type,

            "Manufacturing_Year": year,

            "Color": color

        })

        vehicle_no += 1

df = pd.DataFrame(vehicles)

df.to_csv(DATASET_FOLDER / "vehicles.csv", index=False)

print(df.head())

print(f"\nTotal Vehicles : {len(df)}")

print("\nVehicles Generated Successfully.")