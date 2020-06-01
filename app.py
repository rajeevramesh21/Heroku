import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


app = Flask(__name__)
df=pd.read_excel('New Microsoft Excel Worksheet.xlsx')
model = pickle.load(open('salmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
                           

if __name__ == "__main__":
    app.run(debug=True)