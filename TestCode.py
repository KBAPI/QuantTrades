import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:\PythonTraining\Salary_Data.csv')
x = data['YearsExperience']
y = data['Salary']
#print (data)
b1_num =(( x-x.mean())*(y - y.mean())).sum()
b1_den =((x-x.mean())**2).sum()
b1 = b1_num/b1_den

bo = y.mean()-(b1*x.mean())

#print (bo, b1)

pred = bo + b1* x
plt.plot(x, pred, color = 'blue')
plt.xlabel('Year of Expereince')
plt.ylabel('Predicted Salary')
plt.scatter(x,y,color = 'RED')
plt.show()
