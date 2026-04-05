# recognizers.py

from presidio_analyzer import PatternRecognizer, Pattern


def get_custom_recognizers():
    recognizers = []

    #  Aadhaar Number (12 digits, optional spaces)
    aadhaar_pattern = Pattern(
        name="aadhaar_pattern",
        regex=r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        score=0.95
    )
    recognizers.append(PatternRecognizer(
        supported_entity="AADHAAR",
        patterns=[aadhaar_pattern]
    ))

    #  PAN Card
    pan_pattern = Pattern(
        name="pan_pattern",
        regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        score=0.95
    )
    recognizers.append(PatternRecognizer(
        supported_entity="PAN",
        patterns=[pan_pattern]
    ))

    #  Driving License (simplified Indian format)
    dl_pattern = Pattern(
        name="dl_pattern",
        regex=r"\b[A-Z]{2}\d{2}\s?\d{11}\b",
        score=0.9
    )
    recognizers.append(PatternRecognizer(
        supported_entity="DRIVING_LICENSE",
        patterns=[dl_pattern]
    ))

    #  Indian Phone Number
    phone_pattern = Pattern(
        name="phone_pattern",
        regex=r"\b[6-9]\d{9}\b",
        score=0.95
    )
    recognizers.append(PatternRecognizer(
        supported_entity="PHONE_NUMBER",
        patterns=[phone_pattern]
    ))

    #  Email (override stronger regex)
    email_pattern = Pattern(
        name="email_pattern",
        regex=r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
        score=0.95
    )
    recognizers.append(PatternRecognizer(
        supported_entity="EMAIL_ADDRESS",
        patterns=[email_pattern]
    ))

    #  IFSC Code
    ifsc_pattern = Pattern(
        name="ifsc_pattern",
        regex=r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        score=0.9
    )
    recognizers.append(PatternRecognizer(
        supported_entity="IFSC_CODE",
        patterns=[ifsc_pattern]
    ))

    #  UPI ID
    upi_pattern = Pattern(
        name="upi_pattern",
        regex=r"\b[\w\.-]+@[a-zA-Z]+\b(?!\.)",
        score=0.85
    )
    recognizers.append(PatternRecognizer(
        supported_entity="UPI_ID",
        patterns=[upi_pattern]
    ))

    #  Bank Account Number (generic)
    bank_pattern = Pattern(
        name="bank_pattern",
        regex=r"\b\d{9,18}\b",
        score=0.7
    )
    recognizers.append(PatternRecognizer(
        supported_entity="BANK_ACCOUNT",
        patterns=[bank_pattern]
    ))

    #  GST Number
    gst_pattern = Pattern(
        name="gst_pattern",
        regex=r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b",
        score=0.9
    )
    recognizers.append(PatternRecognizer(
        supported_entity="GST_NUMBER",
        patterns=[gst_pattern]
    ))

    #  Pincode
    pincode_pattern = Pattern(
        name="pincode_pattern",
        regex=r"\b\d{6}\b",
        score=0.85
    )
    recognizers.append(PatternRecognizer(
        supported_entity="PINCODE",
        patterns=[pincode_pattern]
    ))

    #  Customer ID
    cust_pattern = Pattern(
        name="cust_pattern",
        regex=r"\bCUST\d+\b",
        score=0.8
    )
    recognizers.append(PatternRecognizer(
        supported_entity="CUSTOMER_ID",
        patterns=[cust_pattern]
    ))

    #  Employee ID
    emp_pattern = Pattern(
        name="emp_pattern",
        regex=r"\bEMP\d+\b",
        score=0.8
    )
    recognizers.append(PatternRecognizer(
        supported_entity="EMPLOYEE_ID",
        patterns=[emp_pattern]
    ))

    #  Order ID
    order_pattern = Pattern(
        name="order_pattern",
        regex=r"\bOD\d+\b",
        score=0.85
    )
    recognizers.append(PatternRecognizer(
        supported_entity="ORDER_ID",
        patterns=[order_pattern]
    ))

    return recognizers