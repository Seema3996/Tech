# File to create our own line charts

import pandas as pd
pd.plotting.registers_matplotlib_converters
import matplotlib.pyplot as plt
%matpotlib inline

import seaborn as sns
print("Setup Complete")

#Set up code checking
import os
if not os.path.exists("../input/museum_visitors.csv")
    os.symlink("../input/data-for-datavis/museum_visitors.csv","../input/museum_visitors.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *
print("Setup Complete")


#Load the data

#Path of the file to read
museum_filepath="../input/museum_visitors.csv"

#Read the file into a variable spotify_data
museum_data=pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

#To review the data
museum_data.head()
#number of visitors
ca_museum_jul18 = 2620
avila_oct18 = 19280-4622

# Line chart showing the number of visitors to each museum over time
#To convince the museum board
plt.figure(figsize=(15,6))
plt.title("Number of visitors to each museum over time")

sns.lineplot(data=museum_data["Avila Adobe"],label="Avila Adobe")
sns.lineplot(data=museum_data["Firehouse Museum"],label="Firehouse Museum")
sns.lineplot(data=museum_data["Chinese American Museum"],label="Chinese American Museum")
sns.lineplot(data=museum_data["America Tropical Interpretive Center"],label="ATIC")
plt.show()

#Assesing the seasoning
# Line plot showing the number of visitors to Avila Adobe over time

plt.figure(figsize=(12,6))
plt.title("Monthly visitors to Avila Adobe")
sns.lineplot(data=museum_data['Avila Adobe'])
plt.xlabel("Date")
