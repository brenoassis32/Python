from flask import Flask, render_template, request
from class_taco import *
import cgi
import json
import requests
#import sys

#reload(sys)

#sys.setdefaultencoding('utf-8')

taco=Taco()
global type
type = taco.food_type()
global a 
a = taco.literal_food()
global b
b = taco.literal_energy()
global c
c = taco.literal_protein()
global d
d = taco.literal_fat()
global e
e = taco.literal_carbo()
global f
f = taco.literal_fib()
global g
g = taco.literal_Ca()
global h
h = taco.literal_K()
global I
I = taco.literal_Z()
global J
J = taco.literal_Fe()
global k
k = taco.literal_Mg()
global l
l = taco.literal_Na()
global m
m = taco.literal_Mn()
global n
n = taco.literal_Cu()
global o
o = taco.literal_P()
global p
p = taco.literal_VitC()

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/<user>")
def home(user=None):
    return render_template("home.html", user=user)

@app.route("/shopping/")
def shopping():
    food = taco.food_num_type()
    return render_template("shopping.html", food=food)

@app.route("/my_form/")
def my_form():
    food = taco.food_num()
    return render_template("my-form.html",food=food)

@app.route("/my_form/", methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/teste/', methods=['GET', 'POST'])
def teste():
    alim= a
    lines=[1,2,3,4,5,6]
    others=[7,8,9]
    total=[1,2,3,4,5,6,7,8,9]
    refs=[1,2,3,4,5,6,7,8]
#        new = request.args.get('stat')
#        for i in range(len(type)):
#            if type[i] == new:
#               alim=a[i]
#               print True
#        return render_template("teste.html", type=type, alim=alim )
#	sys.stdout.write(json.dumps({ 'data': request.args.get('stat')}))
#    sys.stdout.write(json.dumps({ 'data': alim}))
    return render_template("teste.html", type=type, alim=alim, a=a , b=b, c=c, d=d, e=e,f=f,g=g,h=h,I=I,J=J,k=k,l=l,m=m,n=n,o=o,p=p, lines=lines, others=others, total=total, refs=refs)

@app.route('/script.js')
def script():
    alim= a
    lines=[1,2,3,4,5,6]
    others=[7,8,9]
    total=[1,2,3,4,5,6,7,8,9]
    refs=[1,2,3,4,5,6,7,8]
    return render_template('script.js', color='pink' , type=type, alim=alim, a=a , b=b, c=c, d=d, e=e,f=f,g=g,h=h,I=I,J=J,k=k,l=l,m=m,n=n,o=o,p=p, lines=lines, others=others, total=total, refs=refs)

@app.route('/polar_area/', methods=['GET', 'POST'])
def polar_area():
    new1 = request.values.get('gramT1') + request.values.get('gramT2') + request.values.get('gramT3') + request.values.get('gramT4') + request.values.get('gramT5') + request.values.get('gramT6') + request.values.get('gramT7') + request.values.get('gramT8') 
    new2 = request.values.get('energT1') + request.values.get('energT2') + request.values.get('energT3') + request.values.get('energT4') + request.values.get('energT5') + request.values.get('energT6') + request.values.get('energT7') + request.values.get('energT8') 
    new3 = request.values.get('proteinT1') + request.values.get('proteinT2') + request.values.get('proteinT3') + request.values.get('proteinT4') + request.values.get('proteinT5') + request.values.get('proteinT6') + request.values.get('proteinT7') + request.values.get('proteinT8') 
    new4 = request.values.get('fatT1') + request.values.get('fatT2') + request.values.get('fatT3') + request.values.get('fatT4') + request.values.get('fatT5') + request.values.get('fatT6') + request.values.get('fatT7') + request.values.get('fatT8') 
    new5 = request.values.get('carbT1') + request.values.get('carbT2') + request.values.get('carbT3') + request.values.get('carbT4') + request.values.get('carbT5') + request.values.get('carbT6') + request.values.get('carbT7') + request.values.get('carbT8') 
    new6 = request.values.get('fibT1') + request.values.get('fibT2') + request.values.get('fibT3') + request.values.get('fibT4') + request.values.get('fibT5') + request.values.get('fibT6') + request.values.get('fibT7') + request.values.get('fibT8') 
    new7 = request.values.get('CaT1') + request.values.get('CaT2') + request.values.get('CaT3') + request.values.get('CaT4') + request.values.get('CaT5') + request.values.get('CaT6') + request.values.get('CaT7') + request.values.get('CaT8') 
    new8 = request.values.get('KT1') + request.values.get('KT2') + request.values.get('KT3') + request.values.get('KT4') + request.values.get('KT5') + request.values.get('KT6') + request.values.get('KT7') + request.values.get('KT8') 
    new9 = request.values.get('ZT1') + request.values.get('ZT2') + request.values.get('ZT3') + request.values.get('ZT4') + request.values.get('ZT5') + request.values.get('ZT6') + request.values.get('ZT7') + request.values.get('ZT8') 
    new10 = request.values.get('FeT1') + request.values.get('FeT2') + request.values.get('FeT3') + request.values.get('FeT4') + request.values.get('FeT5') + request.values.get('FeT6') + request.values.get('FeT7') + request.values.get('FeT8') 
    new11 = request.values.get('MgT1') + request.values.get('MgT2') + request.values.get('MgT3') + request.values.get('MgT4') + request.values.get('MgT5') + request.values.get('MgT6') + request.values.get('MgT7') + request.values.get('MgT8') 
    new12 = request.values.get('NaT1') + request.values.get('NaT2') + request.values.get('NaT3') + request.values.get('NaT4') + request.values.get('NaT5') + request.values.get('NaT6') + request.values.get('NaT7') + request.values.get('NaT8') 
    new13 = request.values.get('MnT1') + request.values.get('MnT2') + request.values.get('MnT3') + request.values.get('MnT4') + request.values.get('MnT5') + request.values.get('MnT6') + request.values.get('MnT7') + request.values.get('MnT8') 
    new14 = request.values.get('CuT1') + request.values.get('CuT2') + request.values.get('CuT3') + request.values.get('CuT4') + request.values.get('CuT5') + request.values.get('CuT6') + request.values.get('CuT7') + request.values.get('CuT8') 
    new15 = request.values.get('PT1') + request.values.get('PT2') + request.values.get('PT3') + request.values.get('PT4') + request.values.get('PT5') + request.values.get('PT6') + request.values.get('PT7') + request.values.get('PT8') 
    new16 = request.values.get('VitCT1') + request.values.get('VitCT2') + request.values.get('VitCT3') + request.values.get('VitCT4') + request.values.get('VitCT5') + request.values.get('VitCT6') + request.values.get('VitCT7') + request.values.get('VitCT8')
    print(new5)
    return render_template('polar_area.html', new1=new1, new2=new2, new3=new3, new4=new4 , new5=new5 , new6=new6, new7=new7 , new8=new8 , new9=new9 , new10=new10 , new11=new11 , new12=new12 , new13=new13 , new14=new14 , new15=new15 , new16=new16)
	
	
if __name__ == '__main__':
    app.run(debug=True)

import os.path
os.path.isfile('home.html') 
