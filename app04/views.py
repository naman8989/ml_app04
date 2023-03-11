from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

import pandas as pd;
import numpy as np;
from sklearn import linear_model;
import seaborn as sb;
from sklearn.linear_model import LogisticRegression;
from sklearn.model_selection import train_test_split;


diaFile = pd.read_csv('app04/diabetes_012_health_indicators_BRFSS2015.csv');

y = diaFile['Diabetes_012'];
x = diaFile.drop(columns='Diabetes_012', axis=1);

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.001,train_size=0.001, random_state=3500)

logReg = linear_model.LogisticRegression(solver='lbfgs', max_iter=99)
logReg.fit(x_train.values,y_train.values)


predictResult = None;

def members(request):
    return HttpResponse("Hello world!")

template = loader.get_template('home.html')
def homePage(request):
    print('in views');
    try:
        if request.method == 'GET':
            print(request.method)

            HighBP = int(request.GET['HighBP']);                             
            HighChol = int(request.GET['HighChol']);
            CholCheck = int(request.GET['CholCheck']);
            bodyBMI = int(request.GET['bodyBMI']);
            Smoker = int(request.GET['Smoker']);
            Stroke = int(request.GET['Stroke']);
            HeartDiseaseAttack = int(request.GET['HeartDiseaseAttack']); 
            PhysActivity = int(request.GET['PhysActivity']);
            Fruits = int(request.GET['Fruits']);
            Veggies = int(request.GET['Veggies']);
            HvyAlcoholCons = int(request.GET['HvyAlcoholCons']);
            AnyHealthCare = int(request.GET['AnyHealthCare']);
            NoDocbcCost = int(request.GET['NoDocbcCost']);
            GenHelth = int(request.GET['GenHelth']);
            MentHlth = int(request.GET['MentHlth']);
            PhyHlth = int(request.GET['PhyHlth']);
            DiffWalk = int(request.GET['DiffWalk']);
            Sex = int(request.GET['Sex']);
            Age = int(request.GET['Age']);
            Education = int(request.GET['Education']); 
            Income = int(request.GET['Income']);
            # print(HighBP,HighChol,CholCheck,bodyBMI,Smoker,Stroke,HeartDiseaseAttack,PhysActivity,Fruits,Veggies,HvyAlcoholCons,AnyHealthCare,NoDocbcCost,GenHelth,MentHlth,PhyHlth,DiffWalk,Sex,Age,Education,Income);               
            # http://127.0.0.1:8080/?HighBP=0&HighChol=0&CholCheck=0&bodyBMI=50&Smoker=1&Stroke=1&HeartDiseaseAttack=1&PhysActivity=0&Fruits=0&Veggies=0&HvyAlcoholCons=1&AnyHealthCare=0&NoDocbcCost=1&GenHelth=5&MentHlth=20&PhyHlth=15&DiffWalk=0&Sex=1&Age=1&Education=3&Income=1
            predictResult = logReg.predict( ( [ [HighBP,HighChol,CholCheck,bodyBMI,Smoker,Stroke,HeartDiseaseAttack,PhysActivity,Fruits,Veggies,HvyAlcoholCons,AnyHealthCare,NoDocbcCost,GenHelth,MentHlth,PhyHlth,DiffWalk,Sex,Age,Education,Income]   ] ) );
            print('predicted Result is :- ',predictResult)

        else:
            print('not in get')
    except:
        print('not found in get')

    send = {'sendResult' :  {'predictResult': np.float64(predictResult[0])} }

    return render(request,'home.html',{'predictResult': predictResult[0]})