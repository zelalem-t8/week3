
# 🚗 AlphaCare Insurance Risk Analytics

## 📊 Project Overview

This repository contains an end-to-end insurance analytics pipeline for AlphaCare Insurance Solutions (ACIS). The project explores historical car insurance data from South Africa to identify low-risk customer segments and optimize pricing strategy. The work includes:

- Data cleaning and exploratory analysis (EDA)
- Data versioning with DVC
- Statistical A/B testing for risk-based segmentation

> **Duration:** June 11 – 17, 2025  
> **Author:** [Your Name]  
> **Organization:** 10 Academy - AIM Week 3

---

## 🎯 Objectives

### Task 1: Exploratory Data Analysis
- Assess data structure and quality
- Identify key performance indicators (KPIs) such as:
  - Claim Frequency
  - Claim Severity
  - Loss Ratio
  - Margin
- Detect missing values and outliers
- Visualize regional and temporal trends

### Task 2: Data Version Control (DVC)
- Initialize reproducible data pipeline
- Track raw and cleaned data with DVC
- Enable auditability for future model training

### Task 3: A/B Hypothesis Testing
- Statistically test risk and profit differences across:
  - Province
  - PostalCode (zip)
  - Gender
- Use ANOVA and T-tests to validate business hypotheses

---

## 🗃️ Repository Structure

```
├── data/
│   └── insurance_data.csv.dvc        # Tracked by DVC
├── notebooks/
│   ├── task1_eda.ipynb               # Exploratory Data Analysis
│   ├── task2_dvc_setup.ipynb         # DVC Initialization
│   └── task3_ab_testing.ipynb        # Hypothesis Testing
├── outputs/
│   └── plots/                        # Visualizations (e.g., null ratios, boxplots)
├── src/
│   └── data_load.py                  # Utility for structured loading
├── dvc.yaml
├── .dvc/config
├── .gitignore
└── README.md
```

---

## 📊 Key Visual Insights

- High null ratios in features like `Rebuilt`, `WrittenOff`, `Converted`, and `CrossBorder`
- Outlier detection in `TotalClaims`, `CustomValueEstimate`, and `TotalPremium`
- Province-level risk variation (e.g., Gauteng showing higher average premiums)

![Null Ratio Chart](outputs/plots/null_values_ratio.png)

---

## 📈 Hypothesis Testing Summary

| Hypothesis         | Test   | p-value | Result            |
|--------------------|--------|---------|-------------------|
| Province vs Risk   | ANOVA  | 0.0284  | ✅ Reject H₀       |
| Zip Code vs Risk   | ANOVA  | 1.0000  | ❌ Fail to Reject H₀ |
| Zip Code vs Margin | ANOVA  | 0.9792  | ❌ Fail to Reject H₀ |
| Gender vs Risk     | T-test | 0.0804  | ❌ Fail to Reject H₀ |

> ✅ We recommend regional premium adjustment based on provincial risk, but not based on gender or zip code.

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/insurance-risk-analytics.git
cd insurance-risk-analytics

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or use .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Initialize DVC
dvc pull
```

---

## 🧪 Tools & Libraries

- `pandas`, `numpy` – data processing
- `matplotlib`, `seaborn` – visualizations
- `scipy.stats` – statistical testing (ANOVA, T-test)
- `dvc` – data version control
- `jupyter` – notebook development

---

## ✅ Deliverables

- 📒 Jupyter Notebooks for Tasks 1–3
- 📊 EDA visualizations and null analysis
- 📁 Tracked data with DVC
- 📄 Hypothesis testing report and interpretation
- 🔁 Reproducible Git + DVC pipeline

---

## 📌 Next Steps

- Task 4: Model claim severity (TotalClaims) using regression
- Build premium prediction framework
- Use SHAP or LIME for model interpretability
- Final report and pricing recommendation for ACIS

---

## 📄 License

This project is for educational purposes under the 10 Academy AIM program.
