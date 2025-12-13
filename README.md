# 🛒 Retail Customer Data Analysis  
### Mini Project using NumPy, Pandas, Matplotlib & Seaborn

This mini-project performs **data cleaning, preprocessing, feature engineering, segmentation, and visualization** on a retail customer dataset using Python.

The project demonstrates skills in:

- Data Cleaning  
- Data Transformation  
- Exploratory Data Analysis (EDA)  
- Customer Segmentation  
- Visualization & Insights  

---

## 📌 **Project Overview**

Retail businesses collect large amounts of customer data.  
This project aims to **clean the dataset**, **derive useful insights**, and **visualize customer behavior**.

### Tasks Performed:
1. Handled missing values  
2. Standardized categorical values  
3. Fixed incorrect data types  
4. Removed invalid or inconsistent rows  
5. Created new calculated fields  
6. Segmented customers into meaningful groups  
7. Visualized the dataset using Matplotlib and Seaborn  

---

## 📁 **Dataset Description**

The dataset contains the following fields:

| Column | Description |
|--------|-------------|
| customer_id | Unique identifier for each customer |
| name | Customer name |
| age | Age of customer |
| gender | M / F / Unknown |
| city | Customer's city |
| total_purchases | Number of purchases |
| amount_spent | Lifetime amount spent |
| signup_date | Date of registration |
| last_purchase_date | Last purchase timestamp |
| membership_level | Basic/Silver/Gold/Platinum |

---

## 🧹 **Data Cleaning Steps**

✔ Converted incorrect data types  
✔ Standardized city, gender, and membership values  
✔ Removed invalid ages (<18 or >100)  
✔ Removed future purchase dates  
✔ Filled missing numerical values  
✔ Cleaned string formatting (title case, whitespace removal)  

---

## 🔧 **Feature Engineering**

New columns generated:

- `customer_tenure_days` – Days since signup  
- `days_since_last_purchase` – Recency metric  
- `total_purchase_value` – total_purchases × amount_spent  
- `high_value` – amount_spent > 50,000  
- `active` – last purchase within 60 days  
- `risk_of_churn` – last purchase > 180 days  
- `young_heavy_spender` – age between 18–35 and high spender  

---

## 📊 **Visualizations**

The following charts were created and saved inside the `plots/` folder:

1. **Age Distribution**  
2. **Amount Spent Distribution**  
3. **Customer Count by City**  
4. **Amount Spent vs Membership Level**

All charts are saved automatically as:

plots/age_distribution.png

plots/amount_spent_distribution.png

plots/customers_by_city.png

plots/amount_spent_by_membership.png




## ▶️ **How to Run the Project**

### 1️⃣ Install Required Libraries  


pip install pandas numpy matplotlib seaborn

2️⃣ Run the Script

python main.py

3️⃣ Output Files Generated

retail_customers_cleaned.csv

customer_segments.csv

All charts saved in /plots folder

📂 Project Structure

│── main.py

│── retail_customers.csv

│── retail_customers_cleaned.csv

│── customer_segments.csv

│── plots/

│       ├── age_distribution.png

│       ├── amount_spent_distribution.png

│       ├── customers_by_city.png

│       └── amount_spent_by_membership.png

🧠 Technologies Used

Python

NumPy

Pandas

Matplotlib

Seaborn

🎯 Conclusion

This project demonstrates the ability to clean, transform, analyze, and visualize real-world data using Python.

The insights generated from customer segmentation can help businesses improve:

Marketing strategies

Customer retention

Personalized offers

Revenue growth

👨‍💻 Author

Chippala Sree Ranganath

B.E. Artificial Intelligence and Machine Learning — MSRIT

Trained under NxtWave CCBP 4.0 Technologies

Focused on data engineering, automation, NumPy pipelines, and scalable system design.

🔗 GitHub: https://github.com/sreeranga-chippala






