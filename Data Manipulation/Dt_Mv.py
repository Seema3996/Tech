import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

dtype = reviews.points.dtype  #dtaatype of points column of dataset
point_strings = reviews.points.astype('str') #Create a Series from entries in the points column, but convert the entries to strings. 

#sometimes the price column is null. How many reviews in the dataset are missing a price?
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

#What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field.
#This field is often missing data, so replace missing values with Unknown. Sort in descending order

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
