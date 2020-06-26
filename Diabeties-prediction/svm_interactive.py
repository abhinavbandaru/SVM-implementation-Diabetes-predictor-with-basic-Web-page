def diabetes_predictor(a, b, c, d):
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
    
    glucose = float(a)
    insulin = float(b)
    bmi = float(c)
    diabetesPedigreeFunction = float(d)
    X_test = pd.DataFrame(data={'Glucose': glucose, 'Insulin': insulin, 'BMI': bmi,
                                'DiabetesPedigreeFunction': diabetesPedigreeFunction}, index=[1])
    y_pred = svclassifier.predict(X_test)
    
    return y_pred[0]
