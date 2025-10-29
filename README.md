# 🛍️ Retail Sales Insights Dashboard

A data analytics project that integrates **Python**, **PostgreSQL**, and **Power BI** to analyze and visualize retail sales performance.

---

## 📂 Project Files
| File | Description |
|------|--------------|
| `data/sales.csv` | Retail dataset containing sales, profit, and budget data |
| `etl/load_data.py` | Python ETL script that uploads CSV data to PostgreSQL |
| `dashboard/Retail_Sales_Insights.pbix` | Power BI dashboard for data visualization |

---

## ⚙️ Tools Used
- **Python** (Pandas, SQLAlchemy) – Data loading and cleaning  
- **PostgreSQL** – Data storage and querying  
- **Power BI** – Interactive dashboards and insights  

---

## 🚀 How It Works
1. Run `load_data.py` to load `sales.csv` into PostgreSQL (`retail_sales_db`).
2. Verify using:
   ```sql
   SELECT * FROM sales_data LIMIT 10;
Connect Power BI to PostgreSQL and create visuals like:

Sales by State, Market, and Product

Profit and Margin Analysis

Budget vs Actual Comparisons

Interactive Matrix and Slicers

📊 Dashboard Highlights

KPIs: Total Sales, Profit, Average Margin

Charts: Sales Trend, Market Share, Product Profit

Filters: State, Market, Product Type, Date
