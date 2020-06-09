import requests
import json
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        city=request.form['city']
    else:
        city='Delhi'
    baseurl='http://api.openweathermap.org/data/2.5/weather'
    p={}
    p['q']=city
    p['units']='metric'
    p['appid']='a2b3831b22b9c181daeb517df4d6d375'
    r=requests.get(baseurl,params=p)
    res=r.json()
    weather={
        'city': p['q'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
        'Temp_max': res['main']['temp_min'],
        'Temp_min': res['main']['temp_max'],
        'Humidity':res['main']['humidity'],
        'Pressure':res['main']['pressure']
    }
    print(weather)
    return render_template('index.html',weather=weather)
