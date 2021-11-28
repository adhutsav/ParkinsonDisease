from flask import Blueprint, json, render_template, jsonify
import pickle
import numpy as np

ser = Blueprint('ser', __name__)

@ser.route('/get_outputs')
def get_outputs():
    artifacts_dir = "./Artifacts/"
    models = ["gaussian_naive_bayes_model", "k_nearest_neighbour", "log_regression_model","svm_model"]
    res = []
    count = 1
    #arr = [ 0.63239631, -0.02731081, -0.87985049,  0.36806203,  0.14406765,  0.49280653, 0.30476869,  0.49170115, -0.3137565,  -0.32592164, -0.25848708, -0.23791175, -0.33873289, -0.25879402, -0.2113724,  -0.61257363,  0.87112118,  0.24786644, 0.19888239, -0.97586547, -0.55160318,  0.07769494]
    arr = np.ones(22)
    input = np.array(arr)

    for model in models:
        file_path = artifacts_dir + model
        print(file_path)
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
    response = jsonify({
        'svm':res[0],
        'log_regression' : res[1], 
        'knn' : res[2],
        'gaussian_NB' : res[3],
        'overall': total
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response