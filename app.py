import time
import numpy as np
from flask import Flask, request, jsonify, render_template
import json
import pickle
import pandas as pd
data_path = "combined.csv"
#model=pickle.load(open('model.pkl','rb'))
f = open('model.pkl', 'rb')
#unpickle the dataframe
model = pickle.load(f)
#close file
f.close()
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction=predict(data['name'])
    #prediction=str(prediction)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     int_features = [x for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('index.html', prediction_text='Your text has {} percent similarity '.format(output))

# python3 -m venv .venv
# source .venv/bin/activate