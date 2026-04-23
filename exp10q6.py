'''Write a Pandas program to find and replace the missing values in a given DataFrame which 
do not have any valuable information. '''

import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily'],
    'score': [12.5, 9, np.nan, np.nan, 9],
    'attempts': [1, 3, 2, 3, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Find missing values
print("\nMissing values in DataFrame:")
print(df.isnull())

# 2. Replace missing values
# Option A: Replace with a specific value (e.g., 0)
df_filled = df.fillna(0)

print("\nDataFrame after replacing NaN with 0:")
print(df_filled)

# Option B: Replace with column mean (for numeric columns)
df['score'] = df['score'].fillna(df['score'].mean())
df['attempts'] = df['attempts'].fillna(df['attempts'].mean())

print("\nDataFrame after replacing NaN with column mean:")
print(df)