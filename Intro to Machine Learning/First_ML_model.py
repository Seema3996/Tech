import pandas as pd

iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data=pd.read_csv(iowa_file_path)

#Setup code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex3 import *
print("Setup Complete")

#Specifying Prediction target
home_data.columns()
y=home_data.SalePrice #SalePrice is the target variable

#Create feature X

feature_names= ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
X=home_data[feature_names]

#Review data
print('Description of X')
X.describe()

print('The top few lines of X')
X.head()

#Specify and fit model
from sklearn.tree imort DecisionTreeRegressor
iowa_model=DecisionTreeRegressor(random_state=1)

#Fit the model
iowa_model.fit(X,y)

# Make predictions
predictions=iowa_model.predict(X)
print(predictions)





