import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# CREATE SAMPLE DATASET
# -------------------------------
np.random.seed(42)

data = pd.DataFrame({
    'Group': np.random.choice(['A', 'B'], size=200),
    'Category': np.random.choice(['X', 'Y'], size=200),
    'Hours_Studied': np.random.randint(1, 10, size=200),
    'Score': np.random.randint(40, 100, size=200)
})

print("Dataset Preview:\n")
print(data.head())

# -------------------------------
# AGGREGATED ANALYSIS
# -------------------------------
print("\n--- Aggregated Analysis ---")
agg_result = data.groupby('Hours_Studied')['Score'].mean()
print(agg_result)

# -------------------------------
# STRATIFIED ANALYSIS
# -------------------------------
print("\n--- Stratified Analysis ---")
strat_result = data.groupby(['Category', 'Hours_Studied'])['Score'].mean()
print(strat_result)

# -------------------------------
# VISUALIZATION
# -------------------------------

# Overall trend
plt.figure(figsize=(8,6))
sns.regplot(data=data, x='Hours_Studied', y='Score')
plt.title("Overall Trend (Aggregated Data)")
plt.show()

# Stratified trend
plt.figure(figsize=(8,6))
sns.lmplot(data=data, x='Hours_Studied', y='Score', hue='Category')
plt.title("Stratified Trend by Category")
plt.show()

# Bar Plot Comparison
plt.figure(figsize=(8,6))
sns.barplot(data=data, x='Category', y='Score')
plt.title("Average Score by Category")
plt.show()
