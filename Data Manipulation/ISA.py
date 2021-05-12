import pandas as pd
reviews=pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder;
binder.bind(globals)
from leanrtools.pandas.indexing_selcting_and_assigning import *
print("Setup complete.")

reviews.head()
# 1. select the description coloumn from reviews and assign it to variable desc
desc=reviews['description'] #or desc=reviews.description

# 2. Selet the first value from the desciption value of reviews and assign it to the varible first_description
first_description=reviews.description[0]

# 3. Select the first row of data (the first record) from reviews, assigning it to the variable first_row
first_row=reviews.iloc[0]

# 4. Select the first 10 values from the description column in reviews assigning the result to variable first_descriptions
first_descriptions=reviews.description.iloc[10] #or desc.head(10) and reviews.loc[:9,"description"]

# 5. Select the records with index labels 1,2,3,5 and 8 assigning the result to the variable sample_reviews
indices=[1,2,3,5,8]
sample_reviews=reviews.loc[indices]

# 6. Create a variable df containing the country,province,region_1,region_2 columns of the records with the index labels 0,1,10 and 100.
#In other words, generate the following DataFrame.

cols=['Country','province','region_1','region_2']
indices=[0,1,10,100]
df=reviews.loc[indices,cols]

# 7. Create a variable df containing the country and variety columns of the first 100 record
cols = ['country', 'variety']
df = reviews.loc[:99, cols]
#or
cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]

# 8. Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines=reviews[reviews.country==Italy]

# 9.Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) 
#for wines from Australia or New Z
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand']))& (reviews.points >= 95)]

ealand.
