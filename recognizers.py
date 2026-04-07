# recognizers.py

from presidio_analyzer import PatternRecognizer, Pattern


def get_custom_recognizers():
    recognizers = []

    # 🔴 Aadhaar Number
    recognizers.append(PatternRecognizer(
        supported_entity="AADHAAR",
        patterns=[Pattern(
            name="aadhaar_pattern",
            regex=r"\b\d{4}\s?\d{4}\s?\d{4}\b",
            score=0.95
        )]
    ))

    # 🔴 PAN Card
    recognizers.append(PatternRecognizer(
        supported_entity="PAN",
        patterns=[Pattern(
            name="pan_pattern",
            regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
            score=0.95
        )]
    ))

    # 🔴 Driving License
    recognizers.append(PatternRecognizer(
        supported_entity="DRIVING_LICENSE",
        patterns=[Pattern(
            name="dl_pattern",
            regex=r"\b[A-Z]{2}\d{2}\s?\d{11}\b",
            score=0.9
        )]
    ))

    # 🔴 Phone Number (India)
    recognizers.append(PatternRecognizer(
        supported_entity="PHONE_NUMBER",
        patterns=[Pattern(
            name="phone_pattern",
            regex=r"\b[6-9]\d{9}\b",
            score=0.95
        )]
    ))

    # 🔴 Email
    recognizers.append(PatternRecognizer(
        supported_entity="EMAIL_ADDRESS",
        patterns=[Pattern(
            name="email_pattern",
            regex=r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
            score=0.95
        )]
    ))

    # 🔴 IFSC Code
    recognizers.append(PatternRecognizer(
        supported_entity="IFSC_CODE",
        patterns=[Pattern(
            name="ifsc_pattern",
            regex=r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
            score=0.9
        )]
    ))

    # 🔴 UPI ID (fixed to avoid email overlap)
    recognizers.append(PatternRecognizer(
        supported_entity="UPI_ID",
        patterns=[Pattern(
            name="upi_pattern",
            regex=r"\b[\w\.-]+@[a-zA-Z]+\b(?!\.)",
            score=0.85
        )]
    ))

    # 🔴 Bank Account (FIXED)
    recognizers.append(PatternRecognizer(
        supported_entity="BANK_ACCOUNT",
        patterns=[Pattern(
            name="bank_pattern",
            regex=r"\b\d{12,18}\b",   # ✅ FIX: no 10-digit match
            score=0.85
        )],
        context=["account", "acc", "bank", "a/c"]  # ✅ context-based filtering
    ))

    # 🟡 GST Number
    recognizers.append(PatternRecognizer(
        supported_entity="GST_NUMBER",
        patterns=[Pattern(
            name="gst_pattern",
            regex=r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b",
            score=0.9
        )]
    ))

    # 🟡 Pincode
    recognizers.append(PatternRecognizer(
        supported_entity="PINCODE",
        patterns=[Pattern(
            name="pincode_pattern",
            regex=r"\b\d{6}\b",
            score=0.85
        )]
    ))

    # 🟡 Customer ID
    recognizers.append(PatternRecognizer(
        supported_entity="CUSTOMER_ID",
        patterns=[Pattern(
            name="cust_pattern",
            regex=r"\bCUST\d+\b",
            score=0.8
        )]
    ))

    # 🟡 Employee ID
    recognizers.append(PatternRecognizer(
        supported_entity="EMPLOYEE_ID",
        patterns=[Pattern(
            name="emp_pattern",
            regex=r"\bEMP\d+\b",
            score=0.8
        )]
    ))

    # 🟡 Order ID
    recognizers.append(PatternRecognizer(
        supported_entity="ORDER_ID",
        patterns=[Pattern(
            name="order_pattern",
            regex=r"\bOD\d+\b",
            score=0.85
        )]
    ))

    return recognizers