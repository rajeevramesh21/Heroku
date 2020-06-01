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
    
    

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
def chart():
    
    fig = px.histogram(df, x='Salary')
    fig.show()
    return render_template('untitled1.html', name = fig.show())
def chart1():
    
    fig1 = px.pie(df,'Age')
    fig1.show()
    return render_template('untitled2.html', name1 = fig1.show())

if __name__ == "__main__":
    app.run(debug=True)