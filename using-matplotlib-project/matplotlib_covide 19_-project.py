import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# case_time_series.csv dataset has 7 column. We will be collecting Daily Confirmed  Daily Recovered and Daily Deceased in variables as array.
data = pd.read_csv('/Users/atnafudargaso/Documents/git_work/using-matplotlib-project/Data-Visualization-using-matplotlib-project/case_time_series.csv')
# print(data) check data by uncomment 

Y = data.iloc[61:,1].values # print out the from 61 row and column 1= confirmed case
#print(Y)
R = data.iloc[61:,3].values
# print out the from 61 row and column 3 = recovered case
D = data.iloc[61:,5].values
# print out the from 61 row and column 1= decased case
X = data.iloc[61:,0]
#print(X)     uncommit and check the result 
 
plt.plot(X,Y)
plt.show()
