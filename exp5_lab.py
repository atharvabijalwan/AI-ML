
import pandas as pd


df = pd.read_csv("data_summary.csv")


print("--- Statistical Summary ---")
print(df.describe())

# 2. Data Types and Memory Info
print(" Data Infomation ---")
df.info()



print("--- Unique Values")
print(df.nunique())