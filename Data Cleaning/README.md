Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. 
It is very important to improve the data quality 
and thus leading to overall productivity.

The above python files describe basic processes involved in Data cleaning.

"Handling_missing_values.py" is a basic python code consisting of the following:
  1. Detecting missing values.
  2. Dropping missing values.
  3. Filling missing values.
 
 Link to the dataset used: https://www.kaggle.com/aparnashastry/building-permit-applications-data
 
 "Scaling_normalizing.py" deal with converting the numeric variables to have helpful properties. Scaling is changing the range of data while normalization is changing the range of distribution of data.
 There are 2 main functions used in this code: 
  1. minmax_scaling
  2. boxcox
 
 Link to the dataset used: https://www.kaggle.com/kemical/kickstarter-projects

"Parsing_dates.py" shows how to make Python recognize dates as composed of day, month and year. Starting with checking the data type of date column and converting it to datetime to displaying the days of dates and plottng it to check the date parsing.
Link to the dataset used: https://www.kaggle.com/smithsonian/volcanic-eruptions to displaying 

"Character_encoding.py" deals with avoiding UnicodeDecodeError while loading CSV files.

"Inconsistent_data_entry.py" deals with fixing typos in the data. It begins with doing some text pre-processing and them using fuzzy matching to correct inconsistent data entry.
