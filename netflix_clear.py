# Netflix Titles Analysis Project
# Author: Anshumaan

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("netflix_titles.csv")

# 2. Basic info
print("=== Dataset Info ===")
print(df.info())
print("\n=== Dataset Summary ===")
print(df.describe())

# Show all columns in head()
pd.set_option('display.max_columns', None)
print("\n=== First 5 Rows ===")
print(df.head())

# 3. Handle missing values (only string columns get 'Unknown')
for col in ['director', 'cast', 'country', 'rating', 'description']:
    df[col].fillna("Unknown", inplace=True)

# 4. Convert and extract date features
df['date_added'] = pd.to_datetime(df['date_added'], errors="coerce")
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['day_added'] = df['date_added'].dt.day
df['weekday_added'] = df['date_added'].dt.day_name()

# Keep release_year as integer
df['release_year'] = pd.to_numeric(df['release_year'], errors="coerce")

print("\n=== Date Conversion Sample ===")
print(df[['title', 'date_added', 'year_added', 'month_added', 'day_added', 'release_year']].head())

# 5. Exploratory Data Analysis
print("\n=== Movies vs TV Shows ===")
print(df['type'].value_counts())

print("\n=== Top 10 Countries with Most Content ===")
print(df['country'].value_counts().head(10))

print("\n=== Most Common Ratings ===")
print(df['rating'].value_counts())

print("\n=== Release Year Distribution (Last 20 years) ===")
print(df['release_year'].value_counts().sort_index().tail(20))

# 6. Visualizations
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar', title="Movies vs TV Shows")
plt.show()

plt.figure(figsize=(8,4))
df['year_added'].value_counts().sort_index().plot(kind='line', marker='o', title="Titles Added per Year")
plt.show()

plt.figure(figsize=(8,5))
df['country'].value_counts().head(10).plot(kind='barh', title="Top 10 Countries with Netflix Content")
plt.show()

# 7. Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'netflix_cleaned.csv'")
