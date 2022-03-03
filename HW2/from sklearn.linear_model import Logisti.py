from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

inputs = {
    'neighbor': {
        'model': KNeighborsClassifier(),
        'parameters': {
            'n_neightbors' : [3,4,5,6,7,8],
            'algorithms': ['ball_tree','auto']
        }
    },
    'regression': {
        'model': LogisticRegression(),
        'parameters': {
            'somthing': [2,3,4,5]
        }
    }
}

model = KNeighborsClassifier()
parameters = {'n_neightbors' : 3, 'algorithms': 'auto'}
model.set_params(**parameters)

model.set_params(n_neightbors=3, algorithms='auto')

# inputs 
# list of models
# list of hyperparameters

scores = []

for model_parameters in inputs: #['neighbor, regression]
    parameters = inputs[model_parameters]['parameters']
    model = inputs[model_parameters]['model']
    
    # build parameter grid
    sets_of_parameters = parameter_grid(parameters) # will need to be defined

    for parameter_set in sets_of_parameters:
        model.set_params(parameter_set)
        metric = k_fold_cross(model, parameters, X, y)
        scores.append(metric)