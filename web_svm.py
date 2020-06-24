import pandas as pd

data = pd.read_csv('diabetes.csv')
data.columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                'DiabetesPedigreeFunction', 'Age', 'Class']
file = open('values.txt', 'r')
ls = file.readlines()
file.close()
data = data[['Glucose', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Class']]
X_train = data.iloc[:, :]
Y_train = X_train.iloc[:, -1].values
X_train = X_train.iloc[:, :-1]
from sklearn.svm import SVC

svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, Y_train)
glucose = float(ls[0])
insulin = float(ls[1])
bmi = float(ls[2])
diabetesPedigreeFunction = float(ls[3])
X_test = pd.DataFrame(data={'Glucose': glucose, 'Insulin': insulin, 'BMI': bmi,
                            'DiabetesPedigreeFunction': diabetesPedigreeFunction}, index=[1])
y_pred = svclassifier.predict(X_test)
y_pred = '1' if y_pred == 1 else '0'
file = open('ans.txt', 'w')
file.write(y_pred)
