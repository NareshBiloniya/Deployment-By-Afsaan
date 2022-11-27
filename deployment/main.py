from flask import Flask, render_template, request
import joblib 

app = Flask(__name__) # initialising the app, __name__ means its the file in which we are working
# app is any var i.e. apple etc.

#load the model
model = joblib.load('final_model.pkl')

print('Working')
print(__name__) # it will print: main.py

@app.route('/') # web page or browser will directly show the returned output 'hello world'
def home():
    #return "hello world"
    return render_template('home.html')

@app.route('/about-us')
def about():
    return 'this is about us page'

@app.route('/contact-us')
def contact():
    return 'contact: mob. 1234567890'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data',methods=['post'])
def get_data():
    #name=request.form.get('first_name')
    #email=request.form.get('email')
    #phone=request.form.get('phone')

    #print(name)
    #print(email)
    #print(phone)
    x1=request.form.get('preg')
    x2=request.form.get('plas')
    x3=request.form.get('pres')
    x4=request.form.get('skin')
    x5=request.form.get('test')
    x6=request.form.get('mass')
    x7=request.form.get('pedi')
    x8=request.form.get('age')


    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    print(x7)
    print(x8)

    data = model.predict([[float(x1),float(x2),float(x3),float(x4),float(x5),float(x6),float(x7),float(x8)]])

    if data[0]==0:
        #print('No diabatic')
        result= 'No diabatic'
    else:
        #print('diabatic')
        result= 'diabatic' 
    return result
    #return "hey i got executed"
    
# run the app 
#app.run()

# server will reload again and again automatically 
#app.run(debug=True) # to avoid the restart of server for every small change, for a small change this file will run automatically
app.run(host='0.0.0.0', port=8080) # this is for AWS vm on putty