import pandas as pd
import numpy as np
import os
import pickle
import yaml

from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv(r'data\processed\train_processed.csv')

X_train = train_data.iloc[:,:-1].values
y_train = train_data.iloc[:,-1].values

# X_train = train_data.drop(columns=['Potability'],axis=1)
# y_train = train_data['Potability']

n_estimators = yaml.safe_load(open("params.yaml"))["model_building"]['n_estimators']

clf = RandomForestClassifier(n_estimators=n_estimators)

clf.fit(X_train,y_train)

pickle.dump(clf,open("model.pkl","wb"))