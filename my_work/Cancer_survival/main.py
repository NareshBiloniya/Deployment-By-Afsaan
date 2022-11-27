import joblib
from flask import Flask, render_template , request

app = Flask(__name__)
model = joblib.load('dumped_model.pkl')

@app.route('/')
def ok():
    return 'type /form in the link to go ahead'

@app.route('/form')
def form():
    #return 'ok ye\n good'
    return render_template('form.html')


@app.route('/data',methods=['post'])
def get_data():

    #x1 = request.form.get('age')
    #x2 = request.form.get('year')
    #x3 = request.form.get('node')

    #print(x1)
    #print(x2)
    #print(x3) 

    #out = model.predict([[float(x1),float(x2),float(x3)]])

    # Now we are trying method to in which no need to write several lines for taking input
    float_features = [float(x) for x in request.form.values()]
    features = [float_features]
    out = model.predict(features)

    print('After prediction output is:',out)

    if out[0]==1:
        result = 'The patient will survive 5 years or longer'
    else:
        result = 'The patient will die within 5 years'
    return result



    #return 'Well Done submit button works'

 

#app.run(debug=True)
app.run()