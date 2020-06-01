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
    
    df['YOE'].value_counts().plot(kind='pie')
    
    fig = px.histogram(df, x='Salary')
    
    

    fig1 = px.pie(df,'Age')
    
    

    return (render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output)),
                           render_template('index.html', name= fig1.show()))

if __name__ == "__main__":
    app.run(debug=True)