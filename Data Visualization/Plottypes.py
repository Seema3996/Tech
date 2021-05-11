import os
if not os.path.exists("../input/spotify.csv"):
  os.symlink("../input/data-for-datavis/spotify.csv", "../input/spotify.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex6 import *
print(Setup Complete")

#path of the file to read
spotify_filepath="../input/spotify.csv"

#Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
      
# Change the style of the figure
sns.set_style("ticks") #other styles:"whitegrid","dark","white","ticks"

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

