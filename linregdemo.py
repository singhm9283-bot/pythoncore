# linear regression is used to predict the fututre data based on the 
#previous data...........#y=mx+c
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([2021,2023,2024])
y=np.array([95,89,80])
plt.scatter(x,y)
plt.show()

myModel=LinearRegression()
slope,intercept,r,p,std_err= stats.linregress(x,y)
# if r value is near by 1, then good model else,bad model.....
print(r)

def myfuturemarks(years):
    return slope*year +intercept
year=2025
predictedmarks=myfuturemarks(year)
print("predicted marks is...",predictedmarks)
