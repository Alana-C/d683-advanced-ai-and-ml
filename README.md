## Progress:
- [x] A
  - [x] A1
  - [ ] A2
  - [x] A3
  - [ ] A4
- [x] B
  - [x] B1
  - [x] B2
  - [x] B3
  - [x] B4
  - [x] B5
  - [x] B6
- [ ] C
  - [ ] C1
  - [ ] C2

### GitLab Repository

A. Create your subgroup and project in "[WGU GitLab Environment](https://lrps.wgu.edu/provision/353990238)" and use the "[WGU Knowledge Center: WGU GitLab Environment](https://cm.wgu.edu/t5/Frequently-Asked-Questions/WGU-GitLab-Environment/ta-p/50512)" webpage to complete the following:

_A1. Clone the project to the IDE._  
A1. The project has been cloned to my selected IDE (PyCharm).

_A2. Commit with a message and push when you complete each requirement listed in parts B1–B7._  
A2. Commits are provided for each requirement in Section B

_Note: You may commit and push whenever you want to back up your changes, even if a requirement is not yet complete._

_A3. Submit a copy of the GitLab repository URL in the "Comments to Evaluator" section when you submit this assessment._  
A3. GitLab Repository URL: https://gitlab.com/wgu-gitlab-environment/student-repos/achr641/d683-advanced-ai-and-ml/-/tree/working

_A4. Submit a copy of the repository branch history retrieved from your repository, which must include the commit messages and dates._
A4. Branch History:  
/img  
/img

_Note: Wait until you have completed all of the following prompts before you create your copy of the repository branch history._

### Development of AI/ML Product

_B. Develop your fully functional AI/ML product that addresses your identified business problem or organizational need from Task 1._

### Data Preprocessing

_B1. Apply preprocessing techniques (e.g., converting categorical variables, data cleaning, handling missing data, and scaling features). When you are done, upload the preprocessed dataset to the GitLab repository._  
B1. The following preprocessing techniques have been applied:
- converting categorical variables to integer notation
- cleaning data
- improving integer encoding
- changing boolean variables to appropriate boolean notation
- checking for invalid data

The preprocessed data is available in the 'mushrooms.csv' file, and the preprocessing code is available in the 'preprocessing.py' file. Both files are available in the data folder.

_Note: Remember to commit with a message and push your work to GitLab._

### Model Training

_B2. Build the AI/ML algorithm._  
B2. The AI/ML algorithm has been built in the 'model.py' file.

_B3. Train the model using the AI/ML algorithm._  
B3. The above model has been trained.

_B4. Evaluate model accuracy using metrics like accuracy, precision, recall, and F1 score._  
B4. Model Has Been Evaluated:
- Accuracy Percentage (number correct / number tested): 100% 
- Precision (number true positive / number true positive + number false positive): 100%
- Recall (number total positive / number total positive + number false negative): 100%
- F1 Score (harmonic mean of precision and recall): 100%

_Note: Remember to commit with a message and push your work to GitLab._

### Model Optimization

_B5. Apply cross-validation techniques._  
B5. Cross-validation techniques (repeated stratified k-fold cross validation and hold validation) have been used to verify that accuracy, precision, recall, and f1 scores remain constant for all folds.

_B6. Use hyperparameter tuning to optimize the model._  
B6. Hyperparameter tuning has been applied by finding the minimum value for hyperparameters "n_estimators" and "max-depth" that matches the evaluation scores in B4. This will make model generation, fitting, and prediction quicker without hurting performance.  
- Optimized n_estimators: 3
- Optimized max_depth: 10


_Note: Remember to commit with a message and push your work to GitLab._

### Readme File

_C.  Complete the README file provided in GitLab to include the following:_

_C1. requirements (software, hardware, etc.)_  
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

_C2. instructions to run the AI/ML application_  
C2. To run this program, 

_D. Demonstrate professional communication in the content and presentation of your submission._