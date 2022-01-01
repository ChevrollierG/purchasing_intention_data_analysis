# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:53:12 2021

@author: guill
"""

from flask import Flask,render_template,request
import pandas as pd
import pickle

path="C:/Users/guill/OneDrive/Bureau/Devoirs/Devoir ESILV A4/Python for data analysis/Projet/"

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('template1.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    numAd=request.form['numAd']
    timeAd=request.form['timeAd']
    numIn=request.form['numIn']
    timeIn=request.form['timeIn']
    numProd=request.form['numProd']
    timeProd=request.form['timeProd']
    bounceRate=request.form['bounceRate']
    exitRate=request.form['exitRate']
    pageValue=request.form['pageValue']
    dayValue=request.form['dayValue']
    month=request.form['month']
    weekend=request.form['weekend']
    os=request.form['os']
    browser=request.form['browser']
    region=request.form['region']
    traffic=request.form['traffic']
    visitor=request.form['visitor']
    prodRel_Combined = int(numProd)/(float(timeProd)+0.00001)
    adRel_Combined = int(numAd)/(float(timeAd)+0.00001)
    inRel_Combined = int(numIn)/(float(timeIn)+0.00001)
    bounceByExit = float(bounceRate)/(float(exitRate)+0.00001)
    data=pd.read_csv(path+"data.csv")
    data = data.drop(data.columns[[0]], axis=1)
    data[:]=0
    data.loc[0]['Administrative_Combined']=float(adRel_Combined)
    data.loc[0]['Informational_Combined']=float(inRel_Combined)
    data.loc[0]['ProductRelated_Combined']=float(prodRel_Combined)
    data.loc[0]['Bounce_by_Exit_Rate']=float(bounceByExit)
    data.loc[0]['PageValues']=float(pageValue)
    data.loc[0]['SpecialDay']=float(dayValue)
    data.loc[0]['Weekend']=bool(weekend)
    data.loc[0][month]=1
    data.loc[0]['OS'+str(os)]=1
    data.loc[0]['Browser'+str(browser)]=1
    data.loc[0]['Region'+str(region)]=1
    data.loc[0]['TrafficType'+str(traffic)]=1
    data.loc[0][visitor]=1
    model=pickle.load(open(path+"model.pickle", 'rb'))
    prediction=model.predict(data)[0]
    if(prediction):
        phrase="the visitor bought something on the internet during this session."
    else:
        phrase="the visitor didn't buy anything on the internet during this session."
    
    return render_template("template2.html",nom=phrase)

if __name__ == "__main__":
    app.run(debug=True)
    