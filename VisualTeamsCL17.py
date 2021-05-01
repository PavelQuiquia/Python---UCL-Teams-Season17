import pandas as pd
import numpy as py
import matplotlib.pyplot as plt


T = pd.read_csv(r'C:\Users\Pavel\Desktop\Python1\Champions League\Season17-18\TeamsCL17.csv')
T.sort_values(by=['goal'], ascending=False).plot.bar(x='teamRegionName', y='goal')
plt.show()
T
