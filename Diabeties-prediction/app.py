from flask import Flask, request
from flask import url_for

from svm_interactive import diabetes_predictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        glucoseConcentration = float(request.form["glucoseConcentration"])
        serumInsulin = float(request.form["serumInsulin"])
        BMI = float(request.form["BMI"])
        diabetesPedgreeFunction = float(request.form["diabetesPedgreeFunction"])
        result = diabetes_predictor(glucoseConcentration, serumInsulin, BMI, diabetesPedgreeFunction)
        # return result
        if (result == 0):
            return '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <link rel="stylesheet" type="text/css" href="static/maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
                    <style> 
                    body{
                    background-color: #a7eda4;
                    }                               
                    </style>
                    </head>
                    <body>
                    <div class="container">
                    <div class="jumbotron">
                      <h1 class="display-4">You are not diabetic!!!</h1>
                      <p class="lead">Continue living a healthy lifestyle.</p>
                      <hr class="my-4">
                      <p>Note: This prediction is only 80% accurate.</p>
                      <p class="lead">
                        <a class="btn btn-primary btn-lg" href="/" role="button">Test Again</a>
                      </p>
                    </div>
                    </div>
                    <script src="static/code.jquery.com/jquery-2.1.4.js"></script>
		            <script src="static/maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
                    </body>
                    </html>

            '''
        else:
            return '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <link rel="stylesheet" type="text/css" href="static/maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
                    <style> 
                    body{
                    background-color: #eda4a4;
                    }                                
                    </style>
                    </head>
                    <body>
                    <div class="container">
                    <div class="jumbotron">
                      <h1 class="display-4">You are diabetic!!!</h1>
                      <p class="lead">You need to adjust your lifestyle, so that you can maintain your health optimally.</p>
                      <hr class="my-4">
                      <p>Note: This prediction is only 80% accurate.</p>
                      <p class="lead">
                        <a class="btn btn-primary btn-lg" href="/" role="button">Test Again</a>
                      </p>
                    </div>
                    </div>
                    <script src="static/code.jquery.com/jquery-2.1.4.js"></script>
		            <script src="static/maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
                    </body>
                    </html>
            '''

    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Contact form</title>
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
        <style>
        html, body {
        min-height: 100%;
        padding: 0;
        margin: 0;
        font-family: Roboto, Arial, sans-serif;
        font-size: 14px;
        color: #666;
        }

        h1 {
        margin: 0 0 20px;
        font-weight: 400;
        color: #1c87c9;
        }

        p {
        margin: 0 0 5px;
        }

        .main-block {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: #1c87c9;
        }

        form {
        padding: 25px;
        margin: 25px;
        box-shadow: 0 2px 5px #f5f5f5;
        background: #f5f5f5;
        }

        .fas {
        margin: 25px 10px 0;
        font-size: 72px;
        color: #fff;
        }

        .fa-envelope {
        transform: rotate(-20deg);
        }

        .fa-at , .fa-mail-bulk{
        transform: rotate(10deg);
        }

        input, textarea {
        width: calc(100% - 18px);
        padding: 8px;
        margin-bottom: 20px;
        border: 1px solid #1c87c9;
        outline: none;
        }

        input::placeholder {
        color: #666;
        }

        button {
        width: 100%;
        padding: 10px;
        border: none;
        background: #1c87c9;
        font-size: 16px;
        font-weight: 400;
        color: #fff;
        }

        button:hover {
        background: #2371a0;
        }

        @media (min-width: 568px) {
        .main-block {
        flex-direction: row;
        }

        .left-part, form {
        width: 50%;
        }

        .fa-envelope {
        margin-top: 0;
        margin-left: 20%;
        }

        .fa-at {
        margin-top: -10%;
        margin-left: 65%;
        }

        .fa-mail-bulk {
        margin-top: 2%;
        margin-left: 28%;
        }

        h1 {
        width: 100%;
        text-align: center;
        }
        input{
        margin-top: 1%;
        margin-bottom: 3%;
        }
        </style>
        </head>
        <body>
        <div class="main-block">
        <form method="POST" action=".">
        <h1>Diabetes Test</h1>
        <div class="info">
        <label for="glucoseConcentration">Please enter your Plasma Glucose Concentration a 2 hours in an oral glucose tolerance test:</label>
        <input type="number" name="glucoseConcentration" id="glucoseConcentration" placeholder="Plasma Glucose Concentration" required min="0">
        <label for="serumInsulin">Please enter your 2-Hour Serum Insulin (mu U/ml):</label>
        <input type="number" name="serumInsulin" id="serumInsulin" placeholder="Serum Insulin" required min="0">
        <label for="BMI">Please enter your BMI:</label>
        <input type="number" step="0.1" name="BMI" id="BMI" placeholder="BMI" required min="0">
        <label for="diabetesPedgreeFunction">Please enter your DiabetesPedigreeFunction:</label>
        <input type="number" step="0.001" name="diabetesPedgreeFunction" id="diabetesPedgreeFunction" placeholder="Diabetes Pedgree Function" required min="0" max="1">
        </div>
        <button type="submit" href="/">Submit</button>
        </form>
        </div>
        </body>
        </html>
    '''
