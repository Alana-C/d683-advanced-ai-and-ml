from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RepeatedStratifiedKFold
from user_interface import *
import pandas as pd
import numpy as np

df = pd.read_csv('data/mushrooms.csv')
X = df.drop('class', axis=1)
y = np.array(df['class'])
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

clf = RandomForestClassifier()
clf.fit(X, y)
print("Accuracy:", accuracy_score(y, clf.predict(X)))
print("Precision:", precision_score(y, clf.predict(X)))
print("Recall:", recall_score(y, clf.predict(X)))
print("F1-score:", f1_score(y, clf.predict(X)))

