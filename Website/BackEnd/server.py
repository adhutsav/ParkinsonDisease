import pickle
import numpy as np


def get_outputs(input):
    artifacts_dir = "./Artifacts/"
    models = ["gaussian_naive_bayes_model", "k_nearest_neighbour", "log_regression_model","svm_model"]
    res = []
    count = 1
    input = np.array(input)

    for model in models:
        file_path = artifacts_dir + model
        with open(file_path, "rb") as f:
            m = pickle.load(f)
            output = m.predict([input])
            output = 1
            if output == 1:
                count += 1
            res.append(output)
    total = 0
    if count == 2:
        total = -1
    elif count > 2 :
        total = 1

    ans ={  
        'svm':res[0],
        'log_regression' : res[1], 
        'knn' : res[2],
        'gaussian_NB' : res[3],
        'overall': total
    }

    return ans