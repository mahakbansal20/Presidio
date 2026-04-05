# pii_config.py

"""
PII Configuration for Flipkart FDP System
----------------------------------------
This file defines:
1. Entity categories (Customer, Employee, Warehouse, etc.)
2. Risk classification (RED / YELLOW / GREEN)
"""

# 🔴 Risk Classification Mapping
PII_RISK_LEVELS = {
    "RED": [
        "AADHAAR",
        "PAN",
        "DRIVING_LICENSE",
        "BANK_ACCOUNT",
        "IFSC_CODE",
        "UPI_ID",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "FINANCIAL_INFO"
    ],

    "YELLOW": [
        "FULL_ADDRESS",
        "CUSTOMER_ID",
        "EMPLOYEE_ID",
        "ORDER_ID",
        "LOCATION",
        "GST_NUMBER"
    ],

    "GREEN": [
        "PERSON",
        "CITY",
        "STATE",
        "PINCODE",
        "NAME"
    ]
}


# 🔹 Entity Categories (based on your document)

ENTITY_CATEGORIES = {

    "CUSTOMER_INFORMATION": [
        "PERSON",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "CUSTOMER_ID",
        "AADHAAR",
        "PAN",
        "DRIVING_LICENSE",
        "FULL_ADDRESS",
        "CITY",
        "STATE",
        "PINCODE",
        "UPI_ID",
        "BANK_ACCOUNT",
        "IFSC_CODE"
    ],

    "EMPLOYEE_INFORMATION": [
        "PERSON",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "EMPLOYEE_ID",
        "AADHAAR",
        "PAN",
        "DRIVING_LICENSE",
        "FULL_ADDRESS",
        "CITY",
        "STATE",
        "PINCODE",
        "UPI_ID",
        "BANK_ACCOUNT",
        "IFSC_CODE"
    ],

    "SELLER_VENDOR_INFORMATION": [
        "PERSON",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "GST_NUMBER",
        "FULL_ADDRESS",
        "AADHAAR",
        "PAN",
        "UPI_ID",
        "BANK_ACCOUNT",
        "IFSC_CODE"
    ],

    "WAREHOUSE_INFORMATION": [
        "WAREHOUSE_NAME",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "GST_NUMBER",
        "FULL_ADDRESS",
        "BANK_ACCOUNT",
        "IFSC_CODE"
    ]
}


# 🔹 Priority for Conflict Resolution (IMPORTANT)
ENTITY_PRIORITY = {
    "AADHAAR": 5,
    "PAN": 5,
    "DRIVING_LICENSE": 5,
    "BANK_ACCOUNT": 5,

    "IFSC_CODE": 4,
    "UPI_ID": 4,
    "PHONE_NUMBER": 4,
    "EMAIL_ADDRESS": 4,
    "FINANCIAL_INFO": 4,

    "FULL_ADDRESS": 3,
    "GST_NUMBER": 3,
    "CUSTOMER_ID": 3,
    "EMPLOYEE_ID": 3,
    "ORDER_ID": 3,

    "PERSON": 2,
    "CITY": 1,
    "STATE": 1,
    "PINCODE": 1
}


# 🔹 Helper Function: Get Risk Level
def get_risk_level(entity_type: str) -> str:
    for level, entities in PII_RISK_LEVELS.items():
        if entity_type in entities:
            return level
    return "UNKNOWN"


# 🔹 Helper Function: Get Entity Category
def get_entity_category(entity_type: str) -> str:
    for category, entities in ENTITY_CATEGORIES.items():
        if entity_type in entities:
            return category
    return "OTHER"


# 🔹 Helper Function: Get Priority
def get_priority(entity_type: str) -> int:
    return ENTITY_PRIORITY.get(entity_type, 0)