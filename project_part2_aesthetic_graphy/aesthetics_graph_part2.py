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

# This creates a canvas for the graph where the first value ‘25’ is the width argument position and ‘8’ is the height argument position of the graph.
plt.figure(figsize=(25,8))
 
ax = plt.axes()
# ‘.grid’ function lets you create grid lines across the graph.
# The width of the grid lines can be adjusted by simply passing an argument ‘linewidth’ and changing its color by passing ‘color’ argument.

ax.grid(linewidth=0.4, color='#8f8f8f')
 # late make back color white or red  using the ax.set_facecolor
ax.set_facecolor("red")

# ax.sex_Xlabele = x-axise  arrange in x-axise and choose the color '' .

ax.set_xlabel('\nDate',size=25,color='#4bb4f2')

# ax.set_ylabel information on the y-axise
ax.set_ylabel('Number of Confirmed Cases\n',
              size=25,color='#4bb4f2')
# then plot the graphy
 
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035E9B')
plt.plot(X,Y)
plt.show()