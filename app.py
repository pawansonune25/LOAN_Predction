from operator import methodcaller
import re
from flask import Flask, render_template, request
from numpy.core.fromnumeric import reshape
import config
import numpy as np
from loan_app import function

user = 'pavan'
password ='12345'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('log.html')

@app.route('/login', methods = ['POST'])

def login():
    u1 = str(request.form.get('username'))
    p1 = str(request.form.get('password'))
    
    if user == u1 and password== p1:
        return render_template('index.html')

    else:
        return render_template('log.html')
    # return "pass"

@app.route('/predict',methods = ['POST'])
def loan_app():
    


    gender = int(request.form.get('gender'))
    married = int(request.form.get('married'))
    dependents = int(request.form.get('dependents'))
    education = int(request.form.get('education'))
    Self_Employed = int(request.form.get('self'))
    
    amountterm = int(request.form.get('loanterm'))
    credit = int(request.form.get('credit'))
    parea = int(request.form.get('parea'))
    loanamount = np.log(float(request.form.get('loanamount')))
    
    totalincome = np.log(int(request.form.get('totalincome')))

    print(gender,married,dependents,education,Self_Employed,amountterm,credit,parea,loanamount,totalincome)
    data = np.array([[gender,married,dependents,education,Self_Employed,amountterm,credit,parea,loanamount,totalincome]])
    result =  function.loan_prediction(data)

            
    


    
    return render_template('index.html',loan_result=result)

if __name__ == "__main__":
    app.run(debug=True, host=config.HOST_NAME,port=config.PORT_NUMBER)