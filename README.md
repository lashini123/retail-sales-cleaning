# 🟦 **STEP 1 — Create a new folder for your project**

Example:

```
C:\Users\Asus\Desktop\RetailProject
```

Put your files inside:

* your `.py` files
* dataset (optional)
* README.md (optional)

👉 VS Code is ONLY used to write/edit `.py` files.
Do NOT use VS Code terminal for Git.

---

# 🟦 **STEP 2 — Open GitHub Desktop**

You will see the main screen.

Click:

### ➤ **File → New repository**

Fill the form:

| Field                      | What to write                         |
| -------------------------- | ------------------------------------- |
| **Name**                   | retail-sales-cleaning                 |
| **Local Path**             | browse and select your project folder |
| **Description**            | (optional)                            |
| **Initialize with README** | ❌ uncheck (you already have files)    |

Then click:

### 📌 **Create Repository**

---

# 🟦 **STEP 3 — Add your project files**

Open your project folder in **Explorer** and drag/drop OR copy/paste all files into the repository folder GitHub Desktop created.

Examples:

* `sales_cleaning.py`
* `requirements.txt`
* `.gitignore`
* `README.md`
* `your_dataset.xlsx` (optional)

---

# 🟦 **STEP 4 — Go back to GitHub Desktop**

You will now see:

### ✔ “X changed files”

This means GitHub Desktop detected your pasted project files.

---

# 🟦 **STEP 5 — Make your first commit**

At the bottom-left:

1. **Summary:**

   ```
   Initial commit: add project files
   ```

2. Click **Commit to main**

That’s it. You have a local commit.

---

# 🟦 **STEP 6 — Publish the project to GitHub**

At the top-right in GitHub Desktop, click:

### 🚀 **Publish repository**

Choose:

* Visibility: **Public**
* Do NOT change the name unless needed

Click **Publish Repository**

---

# 🟦 **STEP 7 — Open on GitHub**

After publishing, GitHub Desktop will show a button:

### 🔗 **View on GitHub**

Click it → your project is now online.

---

# 🎉 **DONE! Your project is officially published to GitHub.**



## ⭐ First Time Setup (Run Once Per Project)

Run these in the **VS Code terminal**:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pandas openpyxl
python sales_cleaning.py
```

---

## ⭐ Every Day After (When Returning to Work)

Open VS Code → Open this project → Open terminal → Run:

```powershell
.\venv\Scripts\Activate.ps1
python sales_cleaning.py
```

---

## ⭐ Selecting the Python Interpreter in VS Code (One-Time Click)

1. Look at the **bottom-right** corner of VS Code
2. Click on the Python version
3. Choose this interpreter:

```
.\venv\Scripts\python.exe
```

You only do this once. VS Code will remember it.



---

## ⭐ Notes

* Always make sure `(venv)` appears in the terminal before running your script.
* Never reinstall pandas unless you delete the venv.

---

# 🎉 That’s it — simple and clean!


# 📊 Retail Sales Data Cleaning & Analysis (Python, Pandas)

This project performs **end-to-end cleaning and exploratory analysis** on a real-world retail transactions dataset (Online Retail Dataset – UCI Repository).
The dataset contains **541,909 transactions** and includes product descriptions, quantities, prices, invoice dates, and customer IDs.

---

## 🔧 **Technologies Used**

* Python
* Pandas
* NumPy
* VS Code
* Virtual Environment (venv)

---

## 🚀 **Project Steps**

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

## 🧮 **Feature Engineering**

Created new columns to enable deeper analysis:

| New Column       | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| `TotalPrice`     | `Quantity * UnitPrice` – revenue per line item |
| `Year` / `Month` | For time-based grouping                        |
| `InvoiceMonth`   | Month-level timestamp for trends               |

---

## 📈 **Analysis Highlights**

### **📊 Monthly Sales Trend (Top Months)**

```text
2010-12 → 821,452  
2011-01 → 689,812  
2011-03 → 716,215  
2011-05 → 769,297  
2011-06 → 760,547  
```

### **🏆 Top 10 Products by Revenue**

```text
1. DOTCOM POSTAGE                  £206,248.77  
2. REGENCY CAKESTAND 3 TIER        £174,156.54  
3. PAPER CRAFT , LITTLE BIRDIE     £168,469.60  
4. WHITE HANGING HEART T-LIGHT     £106,236.72  
5. PARTY BUNTING                     £99,445.23  
```

### **🌍 Top 10 Countries by Revenue**

```text
1. United Kingdom     £9,001,744.09  
2. Netherlands          £285,446.34  
3. EIRE                 £283,140.52  
4. Germany              £228,678.40  
5. France               £209,625.37  
```

### **🧑‍🤝‍🧑 Unique Customers**

* **4,338 unique non-null Customer IDs**

---

## 💾 **Export**

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

## 📘 **Project Summary**

This project demonstrates practical, real-world data cleaning and analysis skills:

* Cleaned & validated a large retail dataset (541k rows)
* Removed missing, invalid, and duplicate data
* Engineered analytical features (TotalPrice, Year, Month, InvoiceMonth)
* Performed trend, product, and country-level revenue analysis
* Exported a fully cleaned dataset for further modeling

---

## 📄 **CV Bullet Points**

* Cleaned and analyzed **541k+ retail transactions** using Python and Pandas, reducing noise by removing missing product descriptions, duplicates, and invalid quantities/prices.
* Engineered key analytical features and identified monthly sales trends, top products, and top countries, including **£206k revenue for the top product** and **£9M UK sales**.
* Exported a fully cleaned dataset suitable for dashboards and machine learning workflows.

---

## 📦 Project Structure

```
RetailProject/
│── sales_cleaning.py
│── online_retail.xlsx
│── online_retail_cleaned.csv
│── README.md
└── venv/
```
errors


But the Python code needs the full path including the Excel file, which is:
C:\Users\Asus\Desktop\Data science\Online Retail.xlsx
So your Python code should be:
file_path = r"C:\Users\Asus\Desktop\Data science\Online Retail.xlsx"
df = pd.read_excel(file_path)
print(df.head())

This error means:
👉 Your virtual environment is active ((venv)), but pandas is NOT installed inside it.
Even if you installed pandas before, it must be installed inside this venv.
Let’s fix it in 10 seconds.
________________________________________
✅ STEP 1 — Make sure venv is activated
Your terminal already shows:
(venv) PS C:\Users\Asus\Desktop\Data science>
✔ Good — venv is active.
If (venv) disappears, run:
venv\Scripts\activate
________________________________________
✅ STEP 2 — Install pandas + openpyxl inside the venv
Run this inside your terminal:
pip install pandas openpyxl
You should see messages like:
Installing collected packages: pandas, openpyxl, numpy, etc.
Successfully installed ...
________________________________________
✅ STEP 3 — Verify installation
Run:
pip show pandas
If pandas is installed, you’ll see version info.
________________________________________
✅ STEP 4 — Run your script again
python sales_cleaning.py
________________________________________
Great — the installation worked, but I can see the issue clearly:
👉 Pandas was installed in your global Python (Python310)
👉 But your virtual environment (venv) is not using Python310, it was created from another interpreter.
So even though pandas is installed globally, it's not inside your venv.
That’s why Python says:
ModuleNotFoundError: No module named 'pandas'
Let’s fix it properly.
________________________________________
⭐ FIX: Install pandas into the venv’s own Python
Run this EXACT command:
.\venv\Scripts\python.exe -m pip install pandas openpyxl
This forces the virtual environment’s Python to install pandas.
________________________________________
⭐ Verify it worked
Run:
.\venv\Scripts\python.exe -m pip show pandas
If you see version info → success.
________________________________________
⭐ Then run your script using the venv’s Python:
.\venv\Scripts\python.exe sales_cleaning.py
This guarantees that you're using the Python interpreter inside the venv.



