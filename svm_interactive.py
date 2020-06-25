import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('diabetes.csv')
data.columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                'DiabetesPedigreeFunction', 'Age', 'Class']


data = data[['Glucose', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Class']]
X_train = data.iloc[:, :]
Y_train = X_train.iloc[:, -1].values
X_train = X_train.iloc[:, :-1]
from sklearn.svm import SVC

svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, Y_train)
print('Please Enter the following values:')
glucose = input('Please enter your plasma glucose concentration a 2 hours in an oral glucose tolerance test: ')
insulin = input('Please enter your 2-Hour serum insulin (mu U/ml): ')
bmi = input('Please enter your BMI: ')
diabetesPedigreeFunction = input('Please enter your DiabetesPedigreeFunction: ')
X_test = pd.DataFrame(data={'Glucose': glucose, 'Insulin': insulin, 'BMI': bmi,
                            'DiabetesPedigreeFunction': diabetesPedigreeFunction}, index=[1])
y_pred = svclassifier.predict(X_test)
st = 'You are '
st += "not Diabetic" if y_pred[0] == 0 else "Diabetic"
print()
print(st)
