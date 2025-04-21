#I typically use a .pynb (python notebook like Jupyter) but decided to go with vscode this time

import pandas as pd
import kagglehub
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Usually I would do the following if I have the data on local: df = pd.read_csv("Bestsellers with Categories.csv")

# Decided to use the Kaggle API instead pulling from the author/contributor
path = kagglehub.dataset_download("sootersaalu/amazon-top-50-bestselling-books-2009-2019")

print("Path to dataset files:", path)

# Now that we have the path I am just going to make a path object for readability
csv_path = Path(path) / 'bestsellers with categories.csv'

# Success: I am going to load in and set a df variable now
df = pd.read_csv(csv_path)

# Checking dataset
print(df)

# Exploring data and learning more about it:
# First 5 rows
print(df.head())

# Checking shape of dataset
print(df.shape)

# Getting the columns of the dataset
print(df.columns)

# Getting statistical summary for each column
print(df.describe())

# Now that I have learned a bit more about the data, I will go through some common cleaning steps
# Dropping duplicates: inplace parameter will make changes directly on original DataFrame
df.drop_duplicates(inplace=True)

# Renaming columns for more descrption and readability and printing to confirm changes
df.rename(columns={'Name': 'Title', 'Year': 'Publication Year', 'User Rating': 'Rating', 'Genre': 'Category'}, inplace=True)
print(df.columns)

# djusting data type of some features(columns) for easier manipulation
df["Price"].astype(float)

#Anlayzing Author popularity
author_counts = df['Author'].value_counts()
print(author_counts)

#Average ratings per Genre
avg_rating_genre = df.groupby("Category")["Rating"].mean()
print(avg_rating_genre) #on average user ratings for fiction is +.15 higher than non fiction 

# I can now export these findings into a .csv using the to_csv function
# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_genre.to_csv("avg_rating_by_genre.csv")


# I wanted to play around with visualizations so I made some heatmaps: 
# Ratings of genres and Year and correlation matrix between numerical figures

# How category ratings change over time
pivot_df = df.pivot_table(index="Category", columns="Publication Year", values="Rating", aggfunc="mean")

# Designing visualization:
plt.figure(figsize=(12,9))
custom_colors = ['#FF5A60','#A79B94', '#689EB8']
custom_cmap = LinearSegmentedColormap.from_list("calm_colors", custom_colors)
sns.heatmap(pivot_df, cmap=custom_cmap, annot=True, fmt='.2f')
plt.title("Average Rating by Genre (2009 - 2019)")
plt.show()

# Correlation Heatmap of numerical
# Compute correlation matrix
corr = df[['Rating', 'Reviews', 'Price', 'Publication Year']].corr()

# Designing visualization:
plt.figure(figsize=(12,9))
custom_colors = ['#FF5A60','#A79B94', '#689EB8']
custom_cmap = LinearSegmentedColormap.from_list("calm_colors", custom_colors)
sns.heatmap(corr, cmap=custom_cmap, annot=True, fmt='.2f')
plt.title("Correleation Matrix")
plt.show()
