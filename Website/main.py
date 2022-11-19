from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn import preprocessing

import pickle
app = Flask(__name__)

pipe = pickle.load(open("finalized_model2.sav",'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    district = request.form.get('district')
    housing = request.form.get('housing')
    paper = request.form.get('paper')
    wos = request.form.get('wos')
    province = request.form.get('province')
    size = float(request.form.get('size'))
    floor = float(request.form.get('floor'))
    room = float(request.form.get('room'))

    if request.form.get('width')!='':
        width = float(request.form.get('width'))
    else:
        width = float(0)
    if request.form.get('length')!='':
        length = float(request.form.get('length'))
    else:
         length = float(0)

    print(district, province, housing, paper, wos, size, length, width, room, floor)
    input = pd.DataFrame([[district,province,housing,paper,wos,size,length,width,room,floor]],columns=['District','Province','Type_of_house','Legal_paper','WOS_Segment','Area_fixed','Length_fixed','Width_fixed','Rooms','Floors'])
    RF_prediction = pipe.predict(input)[0]
    print(RF_prediction)

    return str(RF_prediction)+' triệu đồng '
if __name__ == "__main__":
    app.run(debug=True,port=5001)