import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

slices = [62, 142, 195]
activities = ['Travel', 'Place Visit', 'Unknown']
 
cols=['#4C8BE2','#00e061','#fe073a']
exp = [0.2,0.02,0.02]
 
plt.pie(slices,labels=activities,
        textprops=dict(size=25,color='black'),
        radius=3,
        colors=cols,
        autopct='%2.2f%%',
        explode=exp,
        shadow=True,
        startangle=90)
 
plt.title('Transmission\n\n\n\n',color='#4fb4f2',size=40)
plt.show()