"""
Day 11 — Pandas Part 3: Merge + Clean
"""
import pandas as pd
import seaborn as sns
 
df = sns.load_dataset("titanic")
 
#               1. Merging 
# A small lookup table mapping embark_town -> region, to demo merge
region_lookup = pd.DataFrame({
    "embark_town": ["Southampton", "Cherbourg", "Queenstown"],
    "region": ["England", "France", "Ireland"],
})
 
inner_merged = pd.merge(df, region_lookup, on="embark_town", how="inner")
left_merged = pd.merge(df, region_lookup, on="embark_town", how="left")
 
print("original shape:", df.shape)
print("inner merge shape:", inner_merged.shape)   # rows with missing embark_town dropped
print("left merge shape:", left_merged.shape)      # all original rows kept, region = NaN where unmatched
 
#                2. Concatenating 
half1 = df.iloc[:400]
half2 = df.iloc[400:]
recombined = pd.concat([half1, half2])
print("recombined matches original:", recombined.shape[0] == df.shape[0])
 
#                3. apply() + lambda 
def categorize_age(age):
    if pd.isna(age):
        return "unknown"
    elif age < 18:
        return "minor"
    elif age < 60:
        return "adult"
    else:
        return "senior"
 
df["age_group"] = df["age"].apply(categorize_age)
# lambda version of something simpler:
df["fare_doubled"] = df["fare"].apply(lambda x: x * 2)
print(df[["age", "age_group", "fare", "fare_doubled"]].head())
 
#                4. Cleaning 
df_clean = df.rename(columns={"sibsp": "siblings_spouses"})
print(df_clean.dtypes.head())
 
# example dtype fix — pclass is stored as int64 but is really categorical
df_clean["pclass"] = df_clean["pclass"].astype("category")
print(df_clean["pclass"].dtype)
 