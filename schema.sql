DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Pumps;
DROP TABLE IF EXISTS Stations;

CREATE TABLE Stations (
    Station_ID TEXT PRIMARY KEY,
    Station_Name TEXT,
    City TEXT,
    Storage_Capacity_Litres REAL
);

CREATE TABLE Pumps (
    Pump_ID TEXT PRIMARY KEY,
    Station_ID TEXT,
    Pump_Number INTEGER,
    Fuel_Type TEXT,
    Manufacturer TEXT,
    Installation_Year INTEGER,
    Status TEXT,

    FOREIGN KEY (Station_ID)
        REFERENCES Stations(Station_ID)
);

CREATE TABLE Employees (
    Employee_ID TEXT PRIMARY KEY,
    Station_ID TEXT,
    Employee_Name TEXT,
    Gender TEXT,
    Designation TEXT,
    Salary REAL,
    Shift TEXT,
    Joining_Date DATE,
    Status TEXT,

    FOREIGN KEY (Station_ID)
        REFERENCES Stations(Station_ID)
);

CREATE TABLE Customers (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT,
    Gender TEXT,
    Age INTEGER,
    City TEXT,
    Phone_Number TEXT,
    Email TEXT,
    Loyalty_Member TEXT,
    Preferred_Fuel TEXT,
    Preferred_Payment TEXT,
    Monthly_Visits INTEGER,
    Registration_Date DATE
);

CREATE TABLE Vehicles (
    Vehicle_ID TEXT PRIMARY KEY,
    Customer_ID TEXT,
    Registration_Number TEXT,
    Vehicle_Type TEXT,
    Brand TEXT,
    Fuel_Type TEXT,
    Manufacturing_Year INTEGER,
    Color TEXT,

    FOREIGN KEY (Customer_ID)
        REFERENCES Customers(Customer_ID)
);

CREATE TABLE Transactions (
    Transaction_ID TEXT PRIMARY KEY,
    Transaction_Date DATE,
    Transaction_Time TIME,
    Station_ID TEXT,
    Pump_ID TEXT,
    Employee_ID TEXT,
    Customer_ID TEXT,
    Transaction_Type TEXT,
    Vehicle_ID TEXT,
    Container_Type TEXT,
    Fuel_Type TEXT,
    Quantity_Litres REAL,
    Price_Per_Litre REAL,
    Total_Amount REAL,
    Payment_Mode TEXT,
    Loyalty_Points INTEGER,
    Transaction_Status TEXT,
    Weather TEXT,

    FOREIGN KEY (Station_ID)
        REFERENCES Stations(Station_ID),

    FOREIGN KEY (Pump_ID)
        REFERENCES Pumps(Pump_ID),

    FOREIGN KEY (Employee_ID)
        REFERENCES Employees(Employee_ID),

    FOREIGN KEY (Customer_ID)
        REFERENCES Customers(Customer_ID),

    FOREIGN KEY (Vehicle_ID)
        REFERENCES Vehicles(Vehicle_ID)
);