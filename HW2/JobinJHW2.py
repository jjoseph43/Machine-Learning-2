print("hello world");
# Homework 2
import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score # other metrics too pls!
from sklearn.ensemble import RandomForestClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier# more!
from sklearn.model_selection import KFold
from sklearn.model_selection import ParameterGrid
import matplotlib.pyplot as plt

# adapt this code below to run your analysis
# 1. Write a function to take a list or dictionary of clfs and hypers(i.e. use logistic regression), each with 3 different sets of hyper parameters for each
# 2. Expand to include larger number of classifiers and hyperparameter settings
# 3. Find some simple data
# 4. generate matplotlib plots that will assist in identifying the optimal clf and parampters settings
# 5. Please set up your code to be run and save the results to the directory that its executed from
# 6. Investigate grid search function

M = np.array([[1,2],[3,4],[4,5],[4,5],[4,5],[4,5],[4,5],[4,5]])
L = np.ones(M.shape[0])
n_folds = 5

data = (M, L, n_folds)

def run(a_clf, data, clf_hyper={}):
  M, L, n_folds = data # unpack data container
  kf = KFold(n_splits=n_folds) # Establish the cross validation
  ret = {} # classic explication of results

  for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
    clf = a_clf(**clf_hyper) # unpack parameters into clf is they exist
    clf.fit(M[train_index], L[train_index])
    pred = clf.predict(M[test_index])
    ret[ids]= {'clf': clf,
               'train_index': train_index,
               'test_index': test_index,
               'accuracy': accuracy_score(L[test_index], pred)}
  return ret

results = run(RandomForestClassifier, data, clf_hyper={})
#LongLongLiveGridS#LongLon#LLongLiveGridSearch!gLiveGridSearch!
###################################################################

models_dict = {
    "neighbor": KNeighborsClassifier,
    "regression": LogisticRegression,
    "RandomForestClassifier": RandomForestClassifier,
}


#The  three different models imputs
inputs = {
    'neighbor': {
        'model': KNeighborsClassifier(),
        'parameters': {
            'n_neighbors' : [3,4,5,6,7,8],
            "weights":["uniform", "distance"],
            'algorithms': ['ball_tree','auto',"kd_tree"]
            
        }
    },
    'regression': {
        'model': LogisticRegression(),
        'parameters': {
            "penalty":["l1", "l2", "none"]
        }
    },
     'RandomForestClassifier': {
        'model': RandomForestClassifier(),
        'parameters': { "n_estimators": [100, 200, 500, 1000],
        "max_features": ["auto", "sqrt", "log2"],
        "bootstrap": [True],
        "criterion": ["gini", "entropy"],
        "oob_score": [True, False],
            
        }
    }
    
}

################################################################
# Add the run method with data set
#Add the dataset in 

Irisdataset = datasets.load_iris()
M = Irisdataset.data
L = Irisdataset.target
n_folds = 5

data = (M, L, n_folds)

def run(a_clf, data, clf_hyper={}):
  M, L, n_folds = data # unpack data container
  kf = KFold(n_splits=n_folds) # Establish the cross validation
  ret = {} # classic explication of results

  for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
    clf = a_clf(**clf_hyper) # unpack parameters into clf is they exist
    clf.fit(M[train_index], L[train_index])
    pred = clf.predict(M[test_index])
    ret[ids]= {'clf': clf,
               'train_index': train_index,
               'test_index': test_index,
               'accuracy': accuracy_score(L[test_index], pred)}
  return ret

model = KNeighborsClassifier()
parameters = {'n_neighbors' : 3, 'algorithms': 'auto'}
=model.set_params(**parameters)

#model.set_params(n_neightbors=3, algorithms='auto')

# inputs 
# list of models
# list of hyperparameters

scores = []

def parameter_grid(parameters):

for model_parameters in inputs: #['neighbor, regression]
    parameters = inputs[model_parameters]['parameters']
    model = inputs[model_parameters]['model']
    
    # build parameter grid
    sets_of_parameters = parameter_grid(parameters) # will need to be defined

    for parameter_set in sets_of_parameters:
        model.set_params(parameter_set)
        metric = k_fold_cross(model, parameters, X, y)
        scores.append(metric)