import pandas as pd
def classifer():
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
    return svclassifier

def diabetes_predictor(a, b, c, d, svclassifier):
    glucose = float(a)
    insulin = float(b)
    bmi = float(c)
    diabetesPedigreeFunction = float(d)
    X_test = pd.DataFrame(data={'Glucose': glucose, 'Insulin': insulin, 'BMI': bmi,
                                'DiabetesPedigreeFunction': diabetesPedigreeFunction}, index=[1])
    y_pred = svclassifier.predict(X_test)
    st = 'You are '
    st += "not Diabetic" if y_pred[0] == 0 else "Diabetic"

    return st


print('Please Enter the following values:')
a = input('Please enter your plasma glucose concentration a 2 hours in an oral glucose tolerance test: ')
b = input('Please enter your 2-Hour serum insulin (mu U/ml): ')
c = input('Please enter your BMI: ')
d = input('Please enter your DiabetesPedigreeFunction: ')
classifer = classifer()
print(diabetes_predictor(a, b, c, d, classifer))
