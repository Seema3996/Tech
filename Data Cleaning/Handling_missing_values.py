import pandas as pd
import numpy as np

#read in all data
sf_permits=pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv") 

#set seed for reproducibility
np.random.seed(0)

#To print the first five rows of the sf_permits DataFrame
sf_permits.head()  

#Do we have any missing data points. If yes, how many?

missing_values_count=sf_permits.isnull().sum()

#To count the first ten columns
missing_values_count[0:10]

total_cells=np.product(sf_permits.shape)
total_missing=missing_values_count.sum()
percent_missing=(total_missing/total_cells)*100
print(percent_missing)


#dropping missing values:rows

sf_permits.dropna()

#removing al columns with at least one missing value

sf_permits_with_na_dropped=sf_permits.dropna(axis=1)
cols_in_original_dataset=sf_permits.shape[1]
cols_in_na_dropped=sf_permits_with_na_dropped.shape[1]
dropped_coloumns=cols_in_original_dataset-cols_in_na_dropped

print("Columns in original dataset: %d \n" % sf_permits.shape[1])
print("Columns with na's dropped: %d" %sf_permits_with_na_dropped.shape[1])

#Filling in the missing values

sf_permits_with_na_imputed=sf_permits.fillna(method='bfill', axis=0).fillna(0)

