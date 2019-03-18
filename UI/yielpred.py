from flask import Flask, jsonify, request, json
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app)  


@app.route("/postrequest", methods = ['GET','POST'])
def getPostrequest():
    x = request.data
    dataDict = json.loads(x)

    print('Hello'+x+'There')
    print(dataDict)
    return jsonify('result')

if __name__ == '__main__':
    app.run(port=8030)