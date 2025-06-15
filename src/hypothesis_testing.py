# ============================================================================
# Task 3: A/B Hypothesis Testing for Insurance Risk Analytics
# ============================================================================
# Author: Your Name
# Project: 10 Academy - AIM Week 3
# Goal: Statistically test whether risk and profit metrics differ across:
#       - Province
#       - PostalCode (Zip)
#       - Gender
# ============================================================================

import pandas as pd
import numpy as np
from scipy.stats import f_oneway, ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_load import load_data

# ----------------------------
# STEP 1: Load the Dataset
# ----------------------------
file_path = "data/MachineLearningRating_v3.txt"  # Adjust the path as needed
df = load_data(file_path)
# ----------------------------
# STEP 2: Define Metrics
# ----------------------------
df['HasClaim'] = df['TotalClaims'] > 0
df['LossRatio'] = df['TotalClaims'] / (df['TotalPremium'] + 1e-6)  # avoid divide by 0
df['Margin'] = df['TotalPremium'] - df['TotalClaims']

# ----------------------------
# STEP 3: Hypothesis 1 - Province vs Risk
# H₀: There are no risk differences across provinces
# ----------------------------
loss_by_province = [
    group['LossRatio'].dropna()
    for name, group in df.groupby('Province')
    if group['LossRatio'].count() > 10
]

f_stat_prov, p_val_prov = f_oneway(*loss_by_province)
print(f"ANOVA Province: F = {f_stat_prov:.4f}, p = {p_val_prov:.6f}")
# Interpretation: p < 0.05 → Reject H₀ → Provinces have different risk levels

# Optional Plot
plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x='Province', y='LossRatio')
plt.title("Loss Ratio Distribution by Province")
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()
plt.savefig("figures/loss_ratio_by_province.png")
# ----------------------------
# STEP 4: Hypothesis 2 - Zip Code vs Risk
# H₀: There are no risk differences across postal codes
# ----------------------------
top_zips = df['PostalCode'].value_counts()
top_zips = top_zips[top_zips > 20].index

zip_groups = [
    group['LossRatio'].dropna()
    for zip_code, group in df[df['PostalCode'].isin(top_zips)].groupby('PostalCode')
]

f_stat_zip, p_val_zip = f_oneway(*zip_groups)
print(f"ANOVA PostalCode: F = {f_stat_zip:.4f}, p = {p_val_zip:.6f}")

# ----------------------------
# STEP 5: Hypothesis 3 - Zip Code vs Margin
# H₀: There is no margin difference between postal codes
# ----------------------------
margin_groups = [
    group['Margin'].dropna()
    for zip_code, group in df[df['PostalCode'].isin(top_zips)].groupby('PostalCode')
]

f_stat_margin, p_val_margin = f_oneway(*margin_groups)
print(f"ANOVA Margin by Zip: F = {f_stat_margin:.4f}, p = {p_val_margin:.6f}")

# ----------------------------
# STEP 6: Hypothesis 4 - Gender vs Risk
# H₀: There is no risk difference between men and women
# ----------------------------
female_loss = df[df['Gender'] == 'Female']['LossRatio'].dropna()
male_loss = df[df['Gender'] == 'Male']['LossRatio'].dropna()

t_stat_gender, p_val_gender = ttest_ind(female_loss, male_loss, equal_var=False)
print(f"T-test Gender: t = {t_stat_gender:.4f}, p = {p_val_gender:.6f}")

# Optional Plot
plt.figure(figsize=(6, 5))
sns.boxplot(data=df[df['Gender'].isin(['Female', 'Male'])], x='Gender', y='LossRatio')
plt.title("Loss Ratio by Gender")
plt.tight_layout()
# plt.show()
plt.savefig("figures/loss_ratio_by_gender.png")

# ----------------------------
# STEP 7: Summary Table
# ----------------------------
summary = pd.DataFrame({
    "Hypothesis": [
        "Province vs Risk",
        "Zip Code vs Risk",
        "Zip Code vs Margin",
        "Gender vs Risk"
    ],
    "Test": [
        "ANOVA",
        "ANOVA",
        "ANOVA",
        "T-test"
    ],
    "p-value": [
        p_val_prov,
        p_val_zip,
        p_val_margin,
        p_val_gender
    ],
    "Result": [
        "Reject H₀" if p_val_prov < 0.05 else "Fail to Reject H₀",
        "Reject H₀" if p_val_zip < 0.05 else "Fail to Reject H₀",
        "Reject H₀" if p_val_margin < 0.05 else "Fail to Reject H₀",
        "Reject H₀" if p_val_gender < 0.05 else "Fail to Reject H₀"
    ]
})

print("\n--- Hypothesis Testing Summary ---")
print(summary.to_string(index=False))

# ----------------------------
# STEP 8: Save Summary (Optional)
# ----------------------------
summary.to_csv("data/hypothesis_summary.csv", index=False)
