from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn import preprocessing

import pickle
app = Flask(__name__)

pipe = pickle.load(open("finalized_model.sav",'rb'))
def change(price):
    if (len(price)>3) and (len(price)<7):
        if int(price[-3:]) != 0:
            res = price[:-3] + ' tỷ '+ price[-3:] + ' triệu đồng '
        else:
            res = price[:-3] + ' tỷ '
    elif (len(price)<3):
        res = price + ' triệu đồng '
    else:
        res = price[:-3] + '  tỷ ' + price[-3:] + ' triệu đồng '
    return res

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
    if province in ["Quận 1", "Quận 3", "Quận 4", "Quận 5", "Quận 6",
                                        "Quận 8","Quận 10", "Quận 11", "Quận Phú Nhuận",
                                        "Quận Bình Thạnh", "Quận Tân Phú",
                                        "Quận Tân Bình", "Quận Gò Vấp"]:
        center = 'Yes'
    else:
        center = 'No'
    print(district, province, housing, paper, wos, size, length, width, room, floor)
    minn = 10000000000000
    maxx = -1
    for ts in range(1,6):
        input = pd.DataFrame([[district,province,housing,paper,size,length,width,room,floor,ts,center,wos]],columns=['District','Province','Type_of_house','Legal_paper','Area','Length','Width','Rooms','Floors','Weight','Center','WOS_Segment'])
        price = pipe.predict(input)[0]
        maxx = max(price,maxx)
        minn = min(price,minn)

    res_1 = change(str(int(minn)))
    res_2 = change(str(int(maxx)))
    res = res_1 + ' ~ ' + res_2
    return res
if __name__ == "__main__":
    app.run(debug=True,port=5001)