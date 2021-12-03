from flask import Flask, render_template, request
from werkzeug.datastructures import MultiDict
import azure

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        g = request.form.get('Gender')
        m = request.form.get('Married')
        d = request.form.get('Dependants')
        e = request.form.get('Education')
        s = request.form.get('Self_Employed')
        a = request.form.get('ApplicantIncome')
        c = request.form.get('CoapplicantIncome')
        h = request.form.get('Credit_History')
        p = request.form.get('Property_Area')
        l = request.form.get('Loan_Amount_Term')
        amt = azure.userInput(g1=g, m1=m, d1=d, e1=e, s1=s, a1=a, c1=c, h1=h, p1=p, l1=l)
        form_data = MultiDict([('Eligible Loan Amount', amt)])
        return render_template('data.html', form_data=form_data)
