import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Create a dataset with Categorical (City) and Numerical (Age, Salary) data
data = {
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Dehradun'],
    'Age': [25, 30, 22, 28],
    'Salary': [50000, 80000, 45000, 60000]
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)


df_encoded = pd.get_dummies(df, columns=['City'])

print("\n--- After One-Hot Encoding ---")
print(df_encoded)

scaler = StandardScaler()


df_encoded[['Age', 'Salary']] = scaler.fit_transform(df_encoded[['Age', 'Salary']])

print("\n--- After Feature Scaling (Standardized) ---")
print(df_encoded)