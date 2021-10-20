from flask import Flask,jsonify,request
import pickle
import feature_extractor as fe
import numpy as np

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return '<html><body>hello world</body></html>'

def gyroscope_mean(t_gyroscope):
    xmean=np.mean(t_gyroscope[:,0])
    ymean=np.mean(t_gyroscope[:,1])
    zmean=np.mean(t_gyroscope[:,2])
    return xmean,ymean,zmean

@app.route('/send',methods=['POST'])
def get_data_from_app():
    input_json = request.get_json(force=True) 
    #gyroscope=request.json['gyroscope']
    #accelerometer=request.json['accelerometer']
    # hello=request.json['hello']
    shape = list(np.array(input_json['gyroscope']).shape)
    data= fe.extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
    f_2 = data
    #loaded_model = pickle.load(open('knnpickle_file', 'rb'))
    loaded_model = pickle.load(open('lrmodel(3).pkl', 'rb'))
    outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
    gxmean,gymean,gzmean=gyroscope_mean(np.array(input_json['gyroscope']))
    data = np.array(data)
    pred = outputlabel[int(loaded_model.predict(data.reshape(1,81)))]
    # dictToReturn = {'data' : f_2 ,'output': pred,'shape':shape,'gxmean':gxmean,'gymean':gymean,'gzmean':gzmean}
    dictToReturn = {'output': pred,'shape':shape,'gxmean':gxmean,'gymean':gymean,'gzmean':gzmean}
    return jsonify(dictToReturn)
    #return jsonify(gyroscope=gyroscope,accelerometer=accelerometer)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=4000,debug=True)