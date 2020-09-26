import flask
from flask import Flask, render_template, request
#from sklearn.externals 
import joblib


model = joblib.load('dump_model.pkl')
app = Flask(__name__)


@app.route("/")

@app.route("/mainpage")
def index():
    return flask.render_template('mainpage.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        if request.method=='POST':
            incident = request.get_data(cache=False, as_text=True, parse_form_data=True)
            incident_value = int(incident[9])
            print(incident_value)
        
            if not incident: 
                return render_template('mainpage.html', label="No input provided")
        
        
            prediction = model.predict([[incident_value]])
            total_minutes = prediction[0]
            hour = total_minutes//60
            minutes = total_minutes%60
        
            if hour!=0:
                time = ("%s hours %s minutes"%(hour, minutes))
        
                return render_template('mainpage.html', label= time)
            else:
                time = (" %s minutes"%(minutes))
                return render_template('mainpage.html', label= time)
        except:
            abort(404)




if __name__ == '__main__':
    model = joblib.load('dump_model.pkl')
    app.run(debug=True)
