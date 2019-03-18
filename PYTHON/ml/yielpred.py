from flask import Flask, jsonify, request, json
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app) 

import ml_backend
from ml_backend import get_prediction, load_data, get_model

def get_response(test_dict):
    df, features = load_data()
    reg = get_model(df, features)
    #print(df, features)
    test_1 = {}
    for i in test_dict.keys():
        if i not in ['area', 'year'] and i in features:
            test_1[i+'_'+test_dict[i]] = 1
    #test_1 = {'Crop_Urad': 1, 'State_Name_Meghalaya': 1}
    area = test_dict['area']
    #print(test_1)
    pred = get_prediction(reg, test_1, features, area)
    return pred


@app.route("/postrequest", methods = ['GET','POST'])
def getPostrequest():
    x = request.data
    dataDict = json.loads(x)
    #print(dataDict)
    res = get_response(dataDict)
    print(res)
    return jsonify(res[0])

if __name__ == '__main__':
    app.run(port=8030)