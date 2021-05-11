import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")

my_filepath = '../input/nih-chest-xrays-tfrecords/preprocessed_data.csv'

my_data = pd.read_csv(my_filepath)
my_data.head()

#Create a plot
sns.barplot(x=my_data['Pneumothorax'], y=my_data.index
