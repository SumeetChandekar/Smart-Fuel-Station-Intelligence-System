"""
Smart Fuel Station Intelligence System
Configuration File

Author: Sumeet Chandekar
"""

from pathlib import Path

# ==========================
# Project Paths
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_FOLDER = BASE_DIR / "dataset"
SQL_FOLDER = BASE_DIR / "sql"
IMAGE_FOLDER = BASE_DIR / "images"
POWERBI_FOLDER = BASE_DIR / "powerbi"

# ==========================
# Company Details
# ==========================

COMPANY_NAME = "FuelSense Retail Pvt. Ltd."
STATE = "Maharashtra"

# ==========================
# Dataset Size
# ==========================

NUM_STATIONS = 150
NUM_PUMPS = 900
NUM_EMPLOYEES = 1200
NUM_CUSTOMERS = 45000
NUM_TRANSACTIONS = 120000

# ==========================
# Date Range
# ==========================

START_DATE = "2024-01-01"
END_DATE = "2025-12-31"