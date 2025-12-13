import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =============================
# 0) CREATE FOLDER FOR IMAGES
# =============================

PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)

# =============================
# 1) LOAD DATA
# =============================

df = pd.read_csv("retail_customers.csv")
print("Initial Rows:", len(df))

# =============================
# 2) FIX DATA TYPES
# =============================

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['total_purchases'] = pd.to_numeric(df['total_purchases'], errors='coerce')
df['amount_spent'] = pd.to_numeric(df['amount_spent'], errors='coerce')

df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'], errors='coerce')

# =============================
# 3) CLEAN STRING COLUMNS
# =============================

df['name'] = df['name'].astype(str).str.strip().str.title()
df['city'] = df['city'].astype(str).str.strip().str.title()
df['gender'] = df['gender'].astype(str).str.strip().str.title()
df['membership_level'] = df['membership_level'].astype(str).str.strip().str.title()
df['referral_code'] = df['referral_code'].astype(str).str.strip()

# =============================
# 4) STANDARDIZE CATEGORIES
# =============================

city_mapping = {
    "Bangalore": "Bengaluru",
    "Banglore": "Bengaluru",
    "BanGalore": "Bengaluru",
    "B'lore": "Bengaluru",
    "Hyderbad": "Hyderabad"
}
df['city'] = df['city'].replace(city_mapping)

gender_mapping = {
    "Male": "M", "M": "M",
    "Female": "F", "F": "F"
}
df['gender'] = df['gender'].replace(gender_mapping)
df['gender'] = df['gender'].fillna("Unknown")

membership_mapping = {
    "Gold": "Gold",
    "Silver": "Silver",
    "Platinum": "Platinum",
    "Bronze": "Bronze"
}
df['membership_level'] = df['membership_level'].replace(membership_mapping)
df['membership_level'] = df['membership_level'].fillna("Basic")

# =============================
# 5) REMOVE INVALID ROWS
# =============================

df = df[(df['age'].between(18, 100)) | (df['age'].isna())]
df = df[df['amount_spent'] >= 0]
df = df[df['last_purchase_date'] <= pd.Timestamp.today()]

# =============================
# 6) HANDLE MISSING VALUES
# =============================

df['age'] = df['age'].fillna(df['age'].median())
df['amount_spent'] = df['amount_spent'].fillna(0)
df['total_purchases'] = df['total_purchases'].fillna(0)

# =============================
# 7) FEATURE ENGINEERING
# =============================

today = pd.Timestamp.today()

df['customer_tenure_days'] = (today - df['signup_date']).dt.days
df['days_since_last_purchase'] = (today - df['last_purchase_date']).dt.days
df['total_purchase_value'] = df['total_purchases'] * df['amount_spent']

# =============================
# 8) SEGMENTATION
# =============================

df['high_value'] = df['amount_spent'] > 50000
df['active'] = df['days_since_last_purchase'] < 60
df['risk_of_churn'] = df['days_since_last_purchase'] > 180
df['young_heavy_spender'] = (df['age'].between(18, 35)) & (df['amount_spent'] > 40000)

# =============================
# 9) VISUALIZATIONS + SAVE IMAGES
# =============================

sns.set(style="whitegrid")

# ---- Age Distribution ----
plt.figure(figsize=(8,5))
sns.histplot(df['age'], kde=True, color='blue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig(f"{PLOT_DIR}/age_distribution.png")
plt.close()

# ---- Amount Spent Distribution ----
plt.figure(figsize=(8,5))
sns.histplot(df['amount_spent'], kde=True, color='green')
plt.title("Amount Spent Distribution")
plt.xlabel("Amount Spent")
plt.ylabel("Frequency")
plt.savefig(f"{PLOT_DIR}/amount_spent_distribution.png")
plt.close()

# ---- City-wise Customer Count ----
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='city')
plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig(f"{PLOT_DIR}/customers_by_city.png")
plt.close()

# ---- Amount Spent vs Membership ----
plt.figure(figsize=(10,5))
sns.boxplot(data=df, x='membership_level', y='amount_spent')
plt.title("Amount Spent by Membership Level")
plt.xlabel("Membership Level")
plt.ylabel("Amount Spent")
plt.savefig(f"{PLOT_DIR}/amount_spent_by_membership.png")
plt.close()

print("All charts saved in 'plots/'folder.")

# =============================
# 10) SAVE CLEANED OUTPUT FILES
# =============================

df.to_csv("retail_customers_cleaned.csv", index=False)

segments = df[['customer_id', 'high_value', 'active', 'risk_of_churn', 'young_heavy_spender']]
segments.to_csv("customer_segments.csv", index=False)

if os.path.exists("retail_customers_cleaned.csv") and os.path.exists("customer_segments.csv"):
    print("Success! Output files generated.")
else:
    print("Error generating files.")
