### Progress:
- [x] A
  - [x] A1
  - [x] A2
  - [x] A3
  - [ ] A4
- [x] B
  - [x] B1
  - [x] B2
  - [x] B3
  - [x] B4
  - [x] B5
  - [x] B6
- [x] C
  - [x] C1
  - [x] C2

## A: GitLab Repository

A1. The project has been cloned to my selected IDE (PyCharm).

A2. Commits are provided for each requirement in Section B.

A3. GitLab Repository URL: https://gitlab.com/wgu-gitlab-environment/student-repos/achr641/d683-advanced-ai-and-ml/-/tree/working

A4. Branch History:  
/img  
/img

## B: Development of AI/ML Product
### B1: Data Preprocessing

B1. The following preprocessing techniques have been applied:
- converting categorical variables to integer notation
- cleaning data
- improving integer encoding
- changing boolean variables to appropriate boolean notation
- checking for invalid data

The preprocessed data is available in the 'mushrooms.csv' file, and the preprocessing code is available in the 'preprocessing.py' file. Both files are available in the data folder.


### B2-B4: Model Training

B2. The AI/ML algorithm has been built in the 'model.py' file.

B3. The above model has been trained.

B4. Model Has Been Evaluated:
- Accuracy Percentage (number correct / number tested): 100% 
- Precision (number true positive / number true positive + number false positive): 100%
- Recall (number total positive / number total positive + number false negative): 100%
- F1 Score (harmonic mean of precision and recall): 100%

### B5-B6: Model Optimization
B5. Cross-validation techniques (repeated stratified k-fold cross validation and hold validation) have been used to verify that accuracy, precision, recall, and f1 scores remain constant for all folds.  

B6. Hyperparameter tuning has been applied by finding the minimum value for hyperparameters "n_estimators" and "max-depth" that matches the evaluation scores in B4. This will make model generation, fitting, and prediction quicker without hurting performance.  
- Optimized n_estimators: 3
- Optimized max_depth: 10

## C: Readme File

C1. Requirements to run this AI/ML program are as follows:
- The complete code of this program, including:
  - 'data' folder and contents
  - 'misc' folder and contents
  - model.py
  - README.md
- Python 3.13 or newer
- A python environment including the following packages:
  - NumPy
  - Pandas
  - Sklearn
  - MatPlotLib
- A computer capable of running python 3.13 OR a web-based interface for running python projects

C2. To run this program, do the following:

- Ensure all the requirements specified in C1 are met.
- Run model.py as a python program. This can be done using console/terminal commands, or with the aid of an IDE or similar tool.
- To use the model to run predictions:
  - Open 'model.py'
  - Edit the prediction_values dictionary so that it contains the information that will be used to make a prediction. 
    - Use the example mushrooms as a guide on formatting.
    - The attribute types and options are available in the 'category_translations.txt' file
  - Save the file
  - Run 'model.py'
  - The result of the predictions will be output to the console.
