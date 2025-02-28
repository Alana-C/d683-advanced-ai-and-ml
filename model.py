from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RepeatedStratifiedKFold
from user_interface import *
import pandas as pd
import numpy as np

# FUNCTIONS
def print_test_results(model, X, y, title="Test Results"):
    print()
    print(title)
    print("Accuracy:", accuracy_score(y, model.predict(X)))
    print("Precision:", precision_score(y, model.predict(X)))
    print("Recall:", recall_score(y, model.predict(X)))
    print("F1-score:", f1_score(y, model.predict(X)))

df = pd.read_csv('data/mushrooms.csv')
X = df.drop('class', axis=1)
y = np.array(df['class'])

# Coding/Creating the model
clf = RandomForestClassifier()

# Training the model
clf.fit(X, y)

# Evaluating the model
print_test_results(clf, X, y, "All Data:")

# Cross Validation Testing:
# Hold Validation
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
clf.fit(x_train, y_train)
print_test_results(clf, x_test, y_test, "Holdout Validation:")

# Repeated Stratified K Fold Validation
rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
rskf.get_n_splits(X,y)
scores = []
folds = 0
for i, (train_index, test_index) in enumerate(rskf.split(X,y)):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    scores.append(score)
    folds += 1
print("\nRepeated Stratified K Fold Validation Results:")
print("Average accuracy: {:.3f} (+/- {:.3f})".format(np.mean(scores), np.std(scores)))
print("Number of folds: {}".format(folds))