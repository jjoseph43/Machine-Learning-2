from matplotlib import pyplot as plt
from sklearn  import svm , datasets
from sklearn.model_selection import GridSearchCV, cross_val_score
iris = datasets.load_iris()
import numpy as np

################################


cross_val_score(svm.SVC(kernel='linear',C=10,gamma='auto'),iris.data, iris.target, cv=5)

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

model_params = {
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
        'model': LogisticRegression(solver='liblinear',multi_class='auto'),
        'params': {
            'C': [1,5,10],
            "penalty":[ "l2"]
        }
    }
}

scores = []
bestmodel =[]
bestscore = []

for model_name, mp in model_params.items():
    clf =  GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
    clf.fit(iris.data, iris.target)
    scores.append({
        'model': model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    bestmodel.append(
         model_name,)
    bestscore.append(
         clf.best_score_,
    )
    
print(scores)
print(type(scores))
print(bestmodel)
print(type(bestmodel))
print(bestscore)
print(type(bestscore))

bestaccdicts = {}
for i in range(len(bestmodel)):
    bestaccdicts[bestmodel[i]] = bestscore[i]
print(bestaccdicts)

keys = bestaccdicts.keys()
values = bestaccdicts.values()

plt.bar(keys, values)
plt.show()


