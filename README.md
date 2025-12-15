

#  Retail Sales Data Cleaning & Analysis (Python, Pandas)

This project performs **end-to-end cleaning and exploratory analysis** on a real-world retail transactions dataset (Online Retail Dataset – UCI Repository).
The dataset contains **541,909 transactions** and includes product descriptions, quantities, prices, invoice dates, and customer IDs.

---

##  **Technologies Used**

* Python
* Pandas
* NumPy
* VS Code
* Virtual Environment (venv)

---

##  **Project Steps**

### **1. Load Dataset**

Loaded the Excel dataset and inspected:

* head (sample rows)
* data types
* missing values
* dataset shape

### **2. Data Cleaning**

Performed the following cleaning tasks:

| Cleaning Task                     | Description                                            |
| --------------------------------- | ------------------------------------------------------ |
| Drop missing product descriptions | 1,454 rows removed                                     |
| Remove duplicates                 | 5,268 duplicated rows removed                          |
| Remove invalid rows               | 9,725 negative quantities + 584 invalid prices removed |
| Ensure correct data types         | InvoiceDate converted to datetime                      |

After cleaning, **524,878 valid records** remained (from 541,909 original).

---

##  **Feature Engineering**

Created new columns to enable deeper analysis:

| New Column       | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| `TotalPrice`     | `Quantity * UnitPrice` – revenue per line item |
| `Year` / `Month` | For time-based grouping                        |
| `InvoiceMonth`   | Month-level timestamp for trends               |

---

##  **Analysis Highlights**

### ** Monthly Sales Trend (Top Months)**

```text
2010-12 → 821,452  
2011-01 → 689,812  
2011-03 → 716,215  
2011-05 → 769,297  
2011-06 → 760,547  
```

### ** Top 10 Products by Revenue**

```text
1. DOTCOM POSTAGE                  £206,248.77  
2. REGENCY CAKESTAND 3 TIER        £174,156.54  
3. PAPER CRAFT , LITTLE BIRDIE     £168,469.60  
4. WHITE HANGING HEART T-LIGHT     £106,236.72  
5. PARTY BUNTING                     £99,445.23  
```

### ** Top 10 Countries by Revenue**

```text
1. United Kingdom     £9,001,744.09  
2. Netherlands          £285,446.34  
3. EIRE                 £283,140.52  
4. Germany              £228,678.40  
5. France               £209,625.37  
```

### ** Unique Customers**

* **4,338 unique non-null Customer IDs**

---

##  **Export**

A cleaned dataset was exported as:

```
online_retail_cleaned.csv
```

This file is ready for:

* dashboards
* forecasting
* customer segmentation
* machine learning models

---

##  **Project Summary**

This project demonstrates practical, real-world data cleaning and analysis skills:

* Cleaned & validated a large retail dataset (541k rows)
* Removed missing, invalid, and duplicate data
* Engineered analytical features (TotalPrice, Year, Month, InvoiceMonth)
* Performed trend, product, and country-level revenue analysis
* Exported a fully cleaned dataset for further modeling

---

##  **CV Bullet Points**

* Cleaned and analyzed **541k+ retail transactions** using Python and Pandas, reducing noise by removing missing product descriptions, duplicates, and invalid quantities/prices.
* Engineered key analytical features and identified monthly sales trends, top products, and top countries, including **£206k revenue for the top product** and **£9M UK sales**.
* Exported a fully cleaned dataset suitable for dashboards and machine learning workflows.

---

##  Project Structure

```
RetailProject/
│── sales_cleaning.py
│── online_retail.xlsx
│── online_retail_cleaned.csv
│── README.md
└── venv/
```




