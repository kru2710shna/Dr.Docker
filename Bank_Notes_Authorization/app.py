from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Get Absolute path
current_dir = os.path.dirname(os.path.abspath(__file__))
pickle_file_path = os.path.join(current_dir, 'classifier.pkl')

# Load pickle file
with open(pickle_file_path, 'rb') as f:
    classifier = pickle.load(f)

@app.route('/')
def welcome():
    return "Hello This is a classifier Project: Bank Account Authorization"

@app.route('/predict')
def predict_auth():
    variance = float(request.args.get('variance'))
    skewness = float(request.args.get('skewness'))
    curtosis = float(request.args.get('curtosis'))
    entropy = float(request.args.get('entropy'))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is {}".format(prediction)

@app.route('/predict_auth', methods=["POST"])
def predict_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classfier.predict(df_test)
    return "The predicted values is {}".format(list(prediction))


if __name__ == '__main__':
    app.run()