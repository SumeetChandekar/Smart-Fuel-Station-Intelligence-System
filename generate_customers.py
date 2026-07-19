"""
Smart Fuel Station Intelligence System
Generate Customers

Author: Sumeet Chandekar
"""

import random
import pandas as pd
from faker import Faker
from constants import CITIES

from config import DATASET_FOLDER, NUM_CUSTOMERS

fake = Faker("en_IN")
CITIES = [...]

FUEL_TYPES = [
    "Petrol",
    "Diesel",
    "CNG",
    "Premium Petrol"
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Fuel Card"
]

SHIFTS = [
    "Morning",
    "Evening",
    "Night"
]

GENDERS = [
    "Male",
    "Female"
]
from constants import (
    CITIES,
    FUEL_TYPES,
    PAYMENT_MODES,
    SHIFTS,
    GENDERS
)
customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    customer_id = f"CUST{i:06d}"

    name = fake.name()

    gender = random.choice(["Male", "Female"])

    age = random.randint(18, 75)

    city = random.choice(CITIES)

    phone = fake.phone_number()

    email = fake.email()

    loyalty = random.choices(
        ["Yes", "No"],
        weights=[35, 65]
    )[0]

    preferred_fuel = random.choice(FUEL_TYPES)

    preferred_payment = random.choice(PAYMENT_MODES)

    monthly_visits = random.randint(1, 12)

    registration_date = fake.date_between(
        start_date="-8y",
        end_date="today"
    )

    customers.append({

        "Customer_ID": customer_id,
        "Customer_Name": name,
        "Gender": gender,
        "Age": age,
        "City": city,
        "Phone_Number": phone,
        "Email": email,
        "Loyalty_Member": loyalty,
        "Preferred_Fuel": preferred_fuel,
        "Preferred_Payment": preferred_payment,
        "Monthly_Visits": monthly_visits,
        "Registration_Date": registration_date

    })
customer_df = pd.DataFrame(customers)
customer_df.to_csv(
    DATASET_FOLDER/"customers.csv",
    index=False
)    
print(customer_df.head())

print()

print("Customers Generated Successfully.")

print()

print("Total Customers :",len(customer_df))