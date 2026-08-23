"""
Day 12 — Data Visualization 

"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
 
df = sns.load_dataset("titanic")
 
#             1. Matplotlib basics 
plt.figure()
plt.hist(df["age"].dropna())
plt.title("Distribution of Age")
plt.savefig("hist_age.png")
 
plt.figure()
df["embark_town"].value_counts().plot(kind="bar")
plt.title("Passengers per Embarkation Town")
plt.savefig("bar_embark_town.png")
 
plt.figure()
plt.scatter(df["age"], df["fare"])
plt.title("Age vs Fare")
plt.savefig("scatter_age_fare.png")
 
#             2. Customizing 
plt.figure(figsize=(8, 5))
plt.hist(df["fare"].dropna(), bins=30)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.savefig("hist_fare_customized.png")
 
#             3. Seaborn 
plt.figure()
numeric_df = df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap_corr.png")
 
plt.figure()
sns.countplot(data=df, x="pclass")
plt.title("Passenger Count by Class")
plt.savefig("countplot_pclass.png")
 
plt.figure()
sns.boxplot(data=df, x="pclass", y="fare")
plt.title("Fare by Class")
plt.savefig("boxplot_fare_by_class.png")
 
sns.pairplot(df[["age", "fare", "pclass", "survived"]].dropna())
plt.savefig("pairplot.png")
 
print("all charts saved")
 