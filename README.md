## GST Reconciliation & Tax Gap Analysis Tool
A Python and Power BI project that identifies and quantifies GST filing discrepancies between a company's purchase register and the government's GSTR-2A data.

## Problem Statement
In India, businesses claim Input Tax Credit (ITC) based on GST Invoices files by their vendors.
When vendors file incorrect, incomplete, or missing invoices in the government's GSTR-2A, businesses lose their rightful tax credits - directly impacting their bottom line.

Manual reconciliation of hundreds of invoices is time-consuming and error-prone.
This project automates the detection and quantification of three types of GST discrepancies:
- Missing Invoices
- Taxable Amount Mismatches
- GST Rate Mismatches

## What This Project Does
- Simulates a realistic Purchase Register (500 invoices) with Indian vendor data using Python and Faker.
- Simulates a GSTR-2A dataset with intentional errors - missing invoices (15%), amount mismatches (10%), and GST rate mismatches (8%).
- Runs automated reconciliation logic to detect and categorize all discrepancies.
- Quantifies financial impact - total tax credit lost, GST at risk from amount mismatches, GST at risk from rate mismatches.
- Visualizes findings in an interactive Power BI dashboard with slicers for issue type, date range, and vendor.

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Data simulation and reconciliation logic |
| Pandas | Data manipulation and analysis |
| Numpy | Random data generation |
| Faker | Indian vendor and invoice data simulation |
| Power BI | Interactive dashboard and visualization |

## Project Structure
```
gst-reconciliation-tool/
├── data/
│   ├── raw/
│   │   ├── purchase_register.csv
│   │   └── gstr_2a.csv
│   └── processed/
│       ├── missing_invoices.csv
│       ├── amount_mismatch.csv
│       └── gst_rate_mismatch.csv
├── scripts/
│   ├── simulate_data.py
│   └── reconciliation.py
├── dashboard/
│   └── gst_reconciliation_dashboard.pbix
├── .gitignore
└── README.md
```

## Key Insights From The Dashboard
- **₹3.01M** in total tax credit lost due to missing vendor invoices.
- **Missing Invoices** are the most common issue - accounting for 52% of all discrepancies.
- **July** recorded the highest spike in reconciliation issues across all categories.
- **GST Amount Mismatches** put ₹62.65K at risk due to incorrect taxable amounts filed by vendors.
- **GST Rate Mismatches** resulted in ₹968.81K at risk due to wrong GST slabs applied.

## How To Run

### Step 1 - Install dependencies
```
pip install pandas numpy faker
```

### Step 2 - Simulate the data
```
cd scripts
python simulate_data.py
```

This generates 'purchase_register.csv' and 'gstr_2a.csv' in 'data/raw/'

### Step 3 - Run Reconciliation
```
python reconciliation.py
```

This generates three output files in 'data/processed/'

### Step 4 - View The Dashboard
Open 'dashboard/gst_reconciliation_dashboard.pbix' in Power BI Desktop and click refresh to load the latest data.