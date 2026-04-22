import pandas as pd
import numpy as np


data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Marks': [85, None, 90, 78, 500, 82]  
}
df = pd.DataFrame(data)

print(" Original Data ")
print(df)


df['Marks'] = df['Marks'].fillna(df['Marks'].mean())


Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR


df_cleaned = df[(df['Marks'] >= lower_limit) & (df['Marks'] <= upper_limit)]

print("sorted data below ")
print(df_cleaned)
