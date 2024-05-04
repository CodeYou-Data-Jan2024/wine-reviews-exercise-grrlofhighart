# Create a Python program that reads in the data/winemag-data-130k-v2.csv.zip file.
# Create a summary of the data that contains the name, number of reviews, 
# and the average points for each unique country in the dataset. 
# Write the summary data to a new file in the data folder named reviews-per-country.csv.

import pandas as pd

# read in the data/winemag-data-130k-v2.csv.zip file
data_file = pd.read_csv(r"C:\Users\grrlo\Documents\Projects\wine-reviews-exercise-grrlofhighart\data\winemag-data-130k-v2.csv.zip", index_col=0)

# Review DataFrame and DataFrame info
# data_file
# data_file.info()

# Drop unnecessary columns
data_file = data_file.drop(['description', 'designation', 'price', 'province', 'region_1', 'region_2', 'taster_name','taster_twitter_handle', 'title', 'variety', 'winery'], axis=1)

# Drop rows with missing values
data_file = data_file.dropna(axis=0)

# Create value for the number of reviews for each country
reviews = data_file['country'].value_counts()

# Consolidate rows by Country and Average the total points for each rounding to 1 decimal point
data_file = data_file[["country", "points"]].groupby("country").mean().round(1)

# Create a new DataFrame by connecting "reviews" and
# "data_file" along the columns axis
new_df = pd.concat([reviews, data_file], axis=1)

# Write the data to a new file in the data folder named reviews-per-country.csv
new_df.to_csv(r"C:\Users\grrlo\Documents\Projects\wine-reviews-exercise-grrlofhighart\data\reviews-per-country.csv")
