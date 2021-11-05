from flask import Flask,jsonify,request
import pickle
import feature_extractor as fe
import numpy as np
from tensorflow import keras

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
    N_TIME_STEPS = 100 #sliding window length
    STEP = 50 #Sliding window step size
    N_FEATURES = 12 
    input_json = request.get_json(force=True) 
    gyroscope=request.json['gyroscope']
    acceleromter=request.json['accelerometer']
    accelerometer_gravity=request.json['accelerometer_gravity']
    body=accelerometer-accelerometer_gravity
    li=[gravity,body,gyroscope]
    data=pd.DataFrame(data=li, columns=['Ax','Ay','Az','Lx','Ly','Lz','Gx','Gy','Gz'])
    test_X=fe.concat(data)
    test_X=fe.generate_sequence(test_X,N_TIME_STEPS, STEP)
    X_test=fe.reshape_segments(test_X,N_TIME_STEPS, N_FEATURES)
    model=keras.load_model('keras_model.h5')
    pred=model.predict(X_test)
    # hello=request.json['hello']
    # shape = list(np.array(input_json['gyroscope']).shape)
    # data= fe.extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
    # f_2 = data
    # #loaded_model = pickle.load(open('knnpickle_file', 'rb'))
    # loaded_model = pickle.load(open('lrmodel (5).pkl', 'rb'))
    # outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
    # gxmean,gymean,gzmean=gyroscope_mean(np.array(input_json['gyroscope']))
    # data = np.array(data)
    # pred = outputlabel[int(loaded_model.predict(data.reshape(1,9)))]
    # # dictToReturn = {'data' : f_2 ,'output': pred,'shape':shape,'gxmean':gxmean,'gymean':gymean,'gzmean':gzmean}
    dictToReturn = {'output': pred}

    return jsonify(dictToReturn)
    #return jsonify(gyroscope=gyroscope,accelerometer=accelerometer)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=4000,debug=True)