import pandas as pd

df = pd.read_csv("churn_cleaned.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())
print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum().sum())
print("\nMissing Values by Column:")

missing = df.isnull().sum()

print(missing[missing > 0])
total_customers = len(df)

churned_customers = (df["Churn Label"] == "Yes").sum()

churn_rate = (churned_customers / total_customers) * 100

print("\nTotal Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
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
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.bar(
    contract_analysis.index,
    contract_analysis["churn_rate"]
)

plt.title("Churn Rate by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")

plt.ylim(0, 50)

for i, value in enumerate(contract_analysis["churn_rate"]):
    plt.text(
        i,
        value + 1,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()
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
print(internet_analysis.sort_values("churn_rate", ascending=False))
plt.figure(figsize=(8, 5))

plt.bar(
    internet_analysis.index,
    internet_analysis["churn_rate"]
)

plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")

plt.ylim(0, 50)

for i, value in enumerate(internet_analysis["churn_rate"]):
    plt.text(
        i,
        value + 1,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()
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

payment_analysis = payment_analysis.sort_values(
    "churn_rate",
    ascending=False
)

print("\nChurn by Payment Method:")
print(payment_analysis)
plt.figure(figsize=(9, 5))

plt.bar(
    payment_analysis.index,
    payment_analysis["churn_rate"]
)

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")

plt.xticks(rotation=20, ha="right")
plt.ylim(0, 50)

for i, value in enumerate(payment_analysis["churn_rate"]):
    plt.text(
        i,
        value + 1,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()
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
print("\n========== FINAL CHURN SUMMARY ==========")

print("Total Customers:", len(df))

print(
    "Overall Churn Rate:",
    round((df["Churn Value"].sum() / len(df)) * 100, 2),
    "%"
)

print("\nHighest Churn Contract:")
print(
    contract_analysis["churn_rate"].idxmax(),
    "→",
    contract_analysis["churn_rate"].max(),
    "%"
)

print("\nHighest Churn Internet Service:")
print(
    internet_analysis["churn_rate"].idxmax(),
    "→",
    internet_analysis["churn_rate"].max(),
    "%"
)

print("\nHighest Churn Payment Method:")
print(
    payment_analysis["churn_rate"].idxmax(),
    "→",
    payment_analysis["churn_rate"].max(),
    "%"
)