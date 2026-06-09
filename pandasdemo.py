import pandas as pd

myfriendsAge=[20,21,22,23,24]
dataframe=pd.DataFrame(myfriendsAge)
print(dataframe)

dataframe=dataframe+5
print(dataframe)
print(dataframe.loc[2])
print(dataframe.head())



