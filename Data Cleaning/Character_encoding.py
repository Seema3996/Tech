import pandas as pd
import numpy as np

import chardet

np.random.seed(0)

sample_entry=b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

before=sample_entry.decode("big5-tw")
new_entry=before.encode()

police_killings=pd.read_csv("../input/fatal-police-shootings-in-the-US/PoliceKillingsUS.csv")

police_killings.to_csv("police-killings-utf8.csv")

