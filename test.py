import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('/Users/atnafudargaso/Documents/git_work/using-matplotlib-project/Data-Visualization-using-matplotlib-project/case_time_series.csv')

Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]

plt.plot(X,Y)
plt.show()
