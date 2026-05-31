#(a) Single Level and Hierarchical Indexing :

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df_single = pd.DataFrame(data)

print("Single Level Indexing DataFrame:")
print(df_single)

arrays = [
    ['high', 'high', 'med', 'med', 'low', 'low'],
    ['one', 'two', 'one', 'two', 'one', 'two']
]

index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))

data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [7, 8, 9, 10, 11, 12]
}

df_hierarchical = pd.DataFrame(data, index=index)

print("\nHierarchical Indexing DataFrame:")
print(df_hierarchical)

#(b) Handling Missing Data :

import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
}

df_missing = pd.DataFrame(data)

print("DataFrame with Missing Data:")
print(df_missing)

df_filled = df_missing.fillna(0)

print("\nFilled Missing Data:")
print(df_filled)

df_dropped = df_missing.dropna()

print("\nAfter Dropping Missing Data:")
print(df_dropped)

#(c) Arithmetic and Boolean Operations :

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

df['D'] = df['A'] + df['B']

print("Arithmetic Operation (A + B):")
print(df)

df['E'] = df['C'] > 7

print("\nBoolean Operation (C > 7):")
print(df)

#(d) Merge and Aggregate :

import pandas as pd

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'A': ['A0', 'A1', 'A2']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'B': ['B0', 'B1', 'B2']
})

merged = pd.merge(left, right, on='key')

print("Merged DataFrame:")
print(merged)

data = {
    'A': ['all', 'all', 'in', 'in'],
    'B': ['one', 'two', 'one', 'two'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

aggregated = df.groupby('A').sum()

print("\nAggregated DataFrame:")
print(aggregated)

#(e) Plotting :

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

df['A'].plot(kind='bar', title='Column A')
plt.show()

# (f) Reading and Writing CSV Files :

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print("DataFrame written to CSV")

df_from_csv = pd.read_csv("output.csv")

print("\nDataFrame Read from CSV:")
print(df_from_csv)