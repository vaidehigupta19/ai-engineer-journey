"""
Day 9 — Pandas Part 1: DataFrames 

"""
import pandas as pd
import seaborn as sns

#            1. Creating a DataFrame
data = {"name": ["Asha", "Ravi", "Meera"], "score": [88, 76, 95]}
df_small = pd.DataFrame(data)
print(df_small)

df = sns.load_dataset("titanic")

#            2. First look at the data
print(df.head())
print(df.tail())
print("shape:", df.shape)
print(df.info())
print(df.describe())

#            3. Selecting Columns
ages = df["age"]                      #series
subset = df[["age","fare","sex"]]     #DataFrame

#            4. Selecting rows — loc vs iloc 
# iloc = position-based (integer index, like list slicing)
# loc  = label-based (uses the actual index label, which can be
#        non-integer or reordered — with the default index they
#        often look the same, but they're not the same thing)
fifth_row_iloc = df.iloc[4]
row_by_label = df.loc[4]
rows_10_to_15 = df.iloc[10:16]
 
print(fifth_row_iloc)
print(rows_10_to_15)