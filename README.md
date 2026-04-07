# 🔍 PII Detection System using Presidio

## 📌 Overview

This project is a **Privacy-Preserving PII Detection System** built using **Microsoft Presidio**.
It replaces LLM-based approaches (like Gemini) with a **deterministic, offline, and customizable pipeline** for detecting sensitive data.

The system processes input text or CSV data, identifies Personally Identifiable Information (PII), classifies risk levels, and outputs structured JSON.

---

## 🚀 Features

* ✅ Detects multiple PII types:

  * Phone Numbers
  * Email Addresses
  * Aadhaar, PAN, Driving License
  * Bank Account, IFSC, UPI ID
  * Customer ID, Order ID, GST Number
  * Pincode, Names, etc.

* ✅ Custom recognizers for **Indian-specific PII**

* ✅ Conflict resolution (removes overlapping/wrong detections)

* ✅ Risk classification:

  * 🔴 RED (Highly Sensitive)
  * 🟡 YELLOW (Moderately Sensitive)
  * 🟢 GREEN (Low Risk)

* ✅ Supports:

  * Real-time input (CLI)
  * Batch CSV processing
  * REST API (FastAPI)

* ✅ Ground truth generation + evaluation metrics:

  * TP, FP, FN
  * Precision, Recall, F1 Score
  * Inference time

---

## 🏗️ Project Structure

```
project/
│
├── main.py               # Entry point (CLI + GT builder)
├── api.py                # FastAPI backend
├── evaluation.py        # Evaluation metrics
│
├── analyzer_setup.py    # Presidio analyzer setup
├── recognizers.py       # Custom PII recognizers
├── processor.py         # Core processing pipeline
├── pii_config.py        # Risk + category configuration
│
├── ground_truth.json    # Labeled dataset (generated)
├── input.csv            # Sample input (optional)
├── output.json          # Output results
│
└── requirements.txt     # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahakbansal20/Presidio.git
cd project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install spaCy model

```bash
python -m spacy download en_core_web_lg
```

---

## ▶️ Usage

---

### 🔹 1. Real-Time Detection (CLI)

```bash
python main.py
```

* Enter text manually
* Detect PII instantly
* Option to save as ground truth

---

### 🔹 2. CSV Processing

```bash
python main.py
```

Choose CSV mode and process dataset → outputs JSON.

---

### 🔹 3. Run API Server

```bash
uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

#### Example Request:

```json
{
  "text": "My phone is 9876543210"
}
```

---

## 📊 Evaluation

Run:

```bash
python evaluation.py
```

### Metrics:

* Precision
* Recall
* F1 Score
* Accuracy (limited use)
* Average inference time

---

## 🧠 System Architecture

```
Input (Text / CSV)
        ↓
Presidio Analyzer + Custom Recognizers
        ↓
Filtering + Conflict Resolution
        ↓
Risk Classification Engine
        ↓
Structured JSON Output
```

---

## 🔐 Risk Classification

| Level     | Description                                  |
| --------- | -------------------------------------------- |
| 🔴 RED    | Highly sensitive (Aadhaar, PAN, Phone, Bank) |
| 🟡 YELLOW | Moderate sensitivity (Address, IDs)          |
| 🟢 GREEN  | Low sensitivity (Name, City)                 |

---

## 📈 Key Highlights

* 🔒 Fully offline → No data leakage
* ⚡ Fast inference (milliseconds)
* 🧩 Modular design → Easily extendable
* 🇮🇳 Optimized for Indian datasets
* 🔍 Transparent & explainable decisions

---

## ⚠️ Limitations

* Rule-based → depends on regex quality
* No deep learning fine-tuning (can be extended)
* Requires manual ground truth for evaluation

---

## 🚀 Future Improvements

* Hybrid ML + Presidio model
* Context-aware scoring
* Frontend UI dashboard
* Cloud deployment (AWS / GCP)
* Auto-anonymization (masking PII)

---

## 👨‍💻 Author

**Mahak Bansal**

---

## 📄 License

This project is for academic and research purposes.
