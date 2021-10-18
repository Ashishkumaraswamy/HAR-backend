from flask import Flask,jsonify,request
import pickle
import feature_extractor as fe
import numpy as np

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return '<html><body>hello world</body></html>'

@app.route('/send',methods=['POST'])
def get_data_from_app():
    input_json = request.get_json(force=True) 

    #gyroscope=request.json['gyroscope']
    #accelerometer=request.json['accelerometer']
    # hello=request.json['hello']
    data= fe.extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
    #loaded_model = pickle.load(open('knnpickle_file', 'rb'))
    dictToReturn = {'len' : len(data)}
    return jsonify(dictToReturn)
    #return jsonify(gyroscope=gyroscope,accelerometer=accelerometer)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=4000,debug=True)