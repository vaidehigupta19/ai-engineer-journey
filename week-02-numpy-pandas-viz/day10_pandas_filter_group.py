"""
Day 10 — Pandas Part 2: Filtering + Grouping 
"""
import pandas as pd
import seaborn as sns
 
df = sns.load_dataset("titanic")

#          1. Filtering
adults = df[df["age"] >= 10]
adult_survivors = df[(df["age"] >= 18) & (df["survived"] == 1)]
first_or_third_class = df[(df["pclass"] == 1) | (df["pclass"] == 3)]
 
print("adults:", adults.shape)
print("adult survivors:", adult_survivors.shape)
print("1st or 3rd class:", first_or_third_class.shape)
 
#         2. Sorting & counting 
by_fare_desc = df.sort_values("fare", ascending=False)
print(by_fare_desc[["fare", "pclass"]].head())
 
# value_counts() -> a Series: index = unique values, values = counts
print(df["embark_town"].value_counts())
 
#         3. Grouping 
# Question: what's the average fare per passenger class?
avg_fare_by_class = df.groupby("pclass")["fare"].mean()
print(avg_fare_by_class)
 
count_by_class = df.groupby("pclass")["fare"].count()
print(count_by_class)
 
multi_stats = df.groupby("pclass")["fare"].agg(["mean", "count", "max"])
print(multi_stats)
 
#         4. Missing values 
print(df.isnull().sum())
 
df_dropped = df.dropna()
print("after dropna:", df_dropped.shape)
 
df_filled = df.copy()
df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
print("missing ages left:", df_filled["age"].isnull().sum())