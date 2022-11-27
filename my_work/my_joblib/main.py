import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df=pd.read_csv("Boston_House.csv")
df.drop(["Unnamed: 0"],axis=1,inplace=True)
df.rename(columns={"medv":"Price"},inplace=True)

plt.figure(1,figsize=(14,8)) # figure 1
sns.boxplot(data=df)
#plt.show()

plt.figure(2,figsize=(14,8)) # figure 2
sns.boxplot(y="crim", data=df)
plt.show()
# both the figures will be shownn on screen



print(df.head())








