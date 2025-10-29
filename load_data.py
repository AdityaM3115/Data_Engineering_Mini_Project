import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load CSV
df = pd.read_csv('F:/vscode/Retail_Sales_Insights/data/sales.csv')

# Step 2: Inspect and clean data
print("🔍 Previewing data:")
print(df.head())

# Handle missing values
df.fillna(0, inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 3: Connect to PostgreSQL
# Change credentials as needed (user:password@host:port/db)
engine = create_engine('postgresql://postgres:root@localhost:5432/sales_db')

# Step 4: Upload to PostgreSQL
df.to_sql('sales_data', engine, if_exists='replace', index=False)

print("✅ Data successfully loaded into PostgreSQL database 'sales_db'!")
print(f"📊 Total Rows Uploaded: {len(df)}")
