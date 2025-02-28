from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RepeatedStratifiedKFold
import pandas as pd
import numpy as np

# FUNCTIONS
def test_results(model, X, y, title="Test Results", print_results=True):
    model.fit(X, y)
    accuracy = accuracy_score(y, model.predict(X))
    precision = precision_score(y, model.predict(X))
    recall = recall_score(y, model.predict(X))
    f1 = f1_score(y, model.predict(X))
    if print_results:
        print()
        print(title)
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)
    return accuracy, precision, recall, f1

# Hold Validation
def hold_validation_testing(model, X, y, print_results=True):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    model.fit(x_train, y_train)
    test_results(model, x_test, y_test, "Holdout Validation:", print_results=print_results)

# repeated stratified K Fold Validation
def stratified_k_fold_testing(model, X, y, print_results=True):
    rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    rskf.get_n_splits(X, y)
    scores = []
    folds = 0
    for i, (train_index, test_index) in enumerate(rskf.split(X, y)):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        scores.append(score)
        folds += 1
    if print_results:
        print("\nRepeated Stratified K Fold Validation Results:")
        print("Average accuracy: {:.3f} (+/- {:.3f})".format(np.mean(scores), np.std(scores)))
        print("Number of folds: {}".format(folds))
    return scores

# Hyperparameter Tuning
def hyperparameter_tuning(X, y, n_estimators_list, max_depth_list, print_results=True):
    running = True
    sorted_estimators = sorted(n_estimators_list)
    sorted_depths = sorted(max_depth_list)
    all_scores = []
    for estimator in sorted_estimators:
        for depth in sorted_depths:
            forest = RandomForestClassifier(n_estimators=estimator, max_depth=depth)
            combination_scores = stratified_k_fold_testing(forest, X, y, print_results=False)
            vals = [estimator, depth, np.mean(combination_scores), np.std(combination_scores)]
            if print_results:
                print(f"Estimator: {estimator}, Max Depth: {depth}, Accuracy: {np.mean(combination_scores):.3f} (+/- {np.std(combination_scores):.3f})")
            all_scores.append(vals)
    return sorted(all_scores, key=lambda x: x[2], reverse=True)

df = pd.read_csv('data/mushrooms.csv')
X = df.drop('class', axis=1)
y = np.array(df['class'])
#
# # Coding/Creating the model
# clf = RandomForestClassifier()
#
# # Training the model
# clf.fit(X, y)
#
# # Evaluating the model
# test_results(clf, X, y, "All Data:")
#
# # Cross Validation Testing
# hold_validation_testing(clf, X, y)
# stratified_k_fold_testing(clf, X, y)

# Hyperparameter Tuning
all_scores = hyperparameter_tuning(X, y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], print_results=False)
simplicity_score = all_scores[0][0] * all_scores[0][1]
best_score = all_scores[0][2]
best_option = all_scores[0]
for score_vals in all_scores:
    if score_vals[2] == best_score:
        if score_vals[1]*score_vals[0] < simplicity_score:
            best_option = score_vals
print(best_option)
