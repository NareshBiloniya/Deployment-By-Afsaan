print('ok')
# import the basic library
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#For plotting graphs
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings("ignore")

print('file Path is:\n',os.getcwd())
#print('ok')
df = pd.read_csv('Surgery_survival.csv')
#print(df.head())

# column renaming
df.rename(columns = {'30':'age','64':'year','1':'nodes','1.1':'status'},inplace=True)
print(df.head())

X = df.drop(["status"],axis=1)
y = df["status"]

#train & test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Applying Random Forest Algo
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, random_state=42,n_jobs=-1)
result = model.fit(X_train, y_train)

y_pred_random_forest = model.predict(X_test)

#Calculate accuracy
from sklearn.metrics import accuracy_score
print('Train accuracy:',accuracy_score(y_train, model.predict(X_train)))
print('Test accuracy:',accuracy_score(y_test, y_pred_random_forest))

joblib.dump(model,'dumped_model.pkl')
