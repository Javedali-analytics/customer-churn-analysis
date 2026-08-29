import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("churn_cleaned.csv")

# =========================
# BASIC DATA CHECK
# =========================

print("Column Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nMissing Values by Column:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# =========================
# OVERALL CHURN SUMMARY
# =========================

total_customers = len(df)
churned_customers = df["Churn Value"].sum()
churn_rate = (churned_customers / total_customers) * 100

print("\n========== CHURN SUMMARY ==========")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# =========================
# CHURN BY CONTRACT
# =========================

contract_analysis = (
    df.groupby("Contract")
    .agg(
        total_customers=("CustomerID", "count"),
        churned_customers=("Churn Value", "sum")
    )
)

contract_analysis["churn_rate"] = (
    contract_analysis["churned_customers"]
    / contract_analysis["total_customers"]
    * 100
).round(2)

print("\nChurn by Contract:")
print(contract_analysis)

# Chart
contract_analysis["churn_rate"].sort_values().plot(
    kind="barh",
    figsize=(8, 4)
)

plt.title("Churn Rate by Contract")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Contract")
plt.tight_layout()
plt.show()

# =========================
# CHURN BY INTERNET SERVICE
# =========================

internet_analysis = (
    df.groupby("Internet Service")
    .agg(
        total_customers=("CustomerID", "count"),
        churned_customers=("Churn Value", "sum")
    )
)

internet_analysis["churn_rate"] = (
    internet_analysis["churned_customers"]
    / internet_analysis["total_customers"]
    * 100
).round(2)

print("\nChurn by Internet Service:")
print(internet_analysis)

# Chart
internet_analysis["churn_rate"].sort_values().plot(
    kind="barh",
    figsize=(8, 4)
)

plt.title("Churn Rate by Internet Service")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Internet Service")
plt.tight_layout()
plt.show()

# =========================
# CHURN BY PAYMENT METHOD
# =========================

payment_analysis = (
    df.groupby("Payment Method")
    .agg(
        total_customers=("CustomerID", "count"),
        churned_customers=("Churn Value", "sum")
    )
)

payment_analysis["churn_rate"] = (
    payment_analysis["churned_customers"]
    / payment_analysis["total_customers"]
    * 100
).round(2)

print("\nChurn by Payment Method:")
print(payment_analysis)

# Chart
payment_analysis["churn_rate"].sort_values().plot(
    kind="barh",
    figsize=(9, 5)
)

plt.title("Churn Rate by Payment Method")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Payment Method")
plt.tight_layout()
plt.show()

# =========================
# CHURN BY TENURE
# =========================

tenure_analysis = (
    df.groupby("Tenure Months")
    .agg(
        total_customers=("CustomerID", "count"),
        churned_customers=("Churn Value", "sum")
    )
)

tenure_analysis["churn_rate"] = (
    tenure_analysis["churned_customers"]
    / tenure_analysis["total_customers"]
    * 100
).round(2)

print("\nChurn by Tenure:")
print(tenure_analysis.head(12))

# Chart
plt.figure(figsize=(10, 5))

plt.plot(
    tenure_analysis.index,
    tenure_analysis["churn_rate"],
    marker="o"
)

plt.title("Churn Rate by Tenure")
plt.xlabel("Tenure Months")
plt.ylabel("Churn Rate (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# =========================
# FINAL KEY FINDINGS
# =========================

print("\n========== FINAL KEY FINDINGS ==========")

print(
    "Highest Churn Contract:",
    contract_analysis["churn_rate"].idxmax(),
    "→",
    contract_analysis["churn_rate"].max(),
    "%"
)

print(
    "Highest Churn Internet Service:",
    internet_analysis["churn_rate"].idxmax(),
    "→",
    internet_analysis["churn_rate"].max(),
    "%"
)

print(
    "Highest Churn Payment Method:",
    payment_analysis["churn_rate"].idxmax(),
    "→",
    payment_analysis["churn_rate"].max(),
    "%"
)