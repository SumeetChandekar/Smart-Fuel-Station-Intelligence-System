import pandas as pd
import random
from faker import Faker

from config import DATASET_FOLDER

fake = Faker("en_IN")

stations = pd.read_csv(DATASET_FOLDER / "stations.csv")

employees = []

employee_no = 1

roles = {
    "Manager":1,
    "Cashier":2,
    "Pump Operator":3,
    "Cleaner":1,
    "Security Guard":1
}

salary_range = {
    "Manager":(45000,60000),
    "Cashier":(22000,30000),
    "Pump Operator":(18000,25000),
    "Cleaner":(15000,20000),
    "Security Guard":(18000,22000)
}
for _, station in stations.iterrows():

    station_id = station["Station_ID"]

    for role, count in roles.items():

        for i in range(count):

            employee_id = f"EMP{employee_no:06d}"

            employee_name = fake.name()

            gender = random.choice(["Male", "Female"])

            salary = random.randint(
                salary_range[role][0],
                salary_range[role][1]
            )

            shift = random.choice([
                "Morning",
                "Evening",
                "Night"
            ])

            joining_date = fake.date_between(
                start_date="-6y",
                end_date="today"
            )

            status = random.choices(
                ["Active","On Leave","Resigned"],
                weights=[90,7,3]
            )[0]

            employees.append({
                "Employee_ID": employee_id,
                "Station_ID": station_id,
                "Employee_Name": employee_name,
                "Gender": gender,
                "Designation": role,
                "Salary": salary,
                "Shift": shift,
                "Joining_Date": joining_date,
                "Status": status
            })

            employee_no += 1

df = pd.DataFrame(employees)

df.to_csv(DATASET_FOLDER / "employees.csv", index=False)

print(df.head())

print("\nEmployees Generated Successfully.")           