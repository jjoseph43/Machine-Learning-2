#######
#Jobin Joseph HW2 submission
###
from matplotlib import pyplot as plt
from sklearn import  datasets
from sklearn.model_selection import GridSearchCV, cross_val_score
import numpy as np

################################

# 1. Write a function to take a list or dictionary of CLFs and hypers (i.e. use
#    logistic regression), each with 3 different sets of hyperparameters for
#    each
# 2. Expand to include larger number of classifiers and hyperparameter settings
# 3. Find some simple data
# 4. Generate matplotlib plots that will assist in identifying the optimal CLF
#    and parameters settings
# 5. Please set up your code to be run and save the results to the directory
#    that its executed from
# 6. Investigate grid search function

# practice
# cross_val_score(svm.SVC(kernel='linear',C=10,gamma='auto'),iris.data, iris.target, cv=5)

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Make a dictionary with models and possible parameters to plug in
model_params1 = {
    'KNN': {
        'model': KNeighborsClassifier(),
        'params' : {
            'n_neighbors' : [3,4,5,6,7,8],
            "weights":["uniform", "distance"],
            'algorithm': ['ball_tree','auto',"kd_tree"]
        }  
    },
    'random_forest': {
        'model': RandomForestClassifier(),
        'params' : {
            "n_estimators": [100, 200, 500, 1000],
        "max_features": ["auto", "sqrt", "log2"],
        "bootstrap": [True],
        "criterion": ["gini", "entropy"],
        "oob_score": [True, False],
        }
    },
    'logistic_regression' : {
        'model': LogisticRegression(),
        'params': {
            'C': [1,5,10],
            "penalty":[ "l2"],
            "n_jobs" : [-1,1,5]
        }
    }
}
iris = datasets.load_iris()

#  Made  a  list to be able to put the values from grid search 
# This idea  came from  the TA office hours
def grid_search(model_params,dataset):
    scores = []
    bestmodel =[]
    bestscore = []
 # made a function that can  append into the lists
    for model_name, mp in model_params.items():
        clf =  GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
        clf.fit(dataset.data, dataset.target)
        scores.append({
            'model': model_name,
            'best_score': clf.best_score_,
            'best_params': clf.best_params_
    })
        bestmodel.append(model_name,)
        bestscore.append(clf.best_score_,
    )
    
    print(scores)
    print(type(scores))
    print(bestmodel)
    print(type(bestmodel))
    print(bestscore)
    print(type(bestscore))

# Used the score from the best models and best score 
# join into a dictionary
    bestaccdicts = {}
    for i in range(len(bestmodel)):
        bestaccdicts[bestmodel[i]] = bestscore[i]
    print(bestaccdicts)

    keys = bestaccdicts.keys()
    values = bestaccdicts.values()

# Plotting the values of accuracy by inputing the dictionary
    plt.bar(keys, values)
    ax = plt.gca()

    ax.set_ylim([0.9, 1.0])
    plt.ylabel("Accuracy level")
    plt.xlabel("Models")
    plt.title("Grid search of different models with Iris data set")
    plt.show()

# ready to use function with the input  model list and  data set
grid_search(model_params1, iris)
