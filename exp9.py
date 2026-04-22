import pandas as pd

# 1. Create the imbalanced data
data = {
    'Marks': [90, 85, 88, 70, 40], 
    'Result': ['Pass', 'Pass', 'Pass', 'Pass', 'Fail'] # 4 Pass, 1 Fail
}
df = pd.DataFrame(data)

# Separate them
df_pass = df[df['Result'] == 'Pass']
df_fail = df[df['Result'] == 'Fail']

# --- TECHNIQUE 1: SIMPLE OVERSAMPLING ---
# Just repeat the 'Fail' rows 4 times so it matches the 4 'Pass' rows
df_oversampled = pd.concat([df_pass, df_fail.iloc[[0]*4]]) 

# --- TECHNIQUE 2: SIMPLE UNDERSAMPLING ---
# Just take the first row of 'Pass' to match the 1 'Fail' row
df_undersampled = pd.concat([df_pass.head(1), df_fail])

print("--- Original ---")
print(df['Result'].value_counts())

print("\n--- After Oversampling (Matched Fail to Pass) ---")
print(df_oversampled['Result'].value_counts())

print("\n--- After Undersampling (Matched Pass to Fail) ---")
print(df_undersampled['Result'].value_counts())