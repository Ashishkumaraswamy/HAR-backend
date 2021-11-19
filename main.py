from flask import Flask,jsonify,request
import pickle
import feature_extractor as fe
import numpy as np
from tensorflow import keras
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app=Flask(__name__)

def predict_label(pred,output):
    pred=pred[0].tolist()
    if pred[4]>=0.1:
        return "Standing"
    elif np.argmax(pred)==1 or np.argmax(pred)==5:
        if pred[6]==0:
            return output[np.argmax(pred)]
        else:
            return "Walking"
    else:
        return output[np.argmax(pred)]

@app.route('/',methods=['GET'])
def home():
    return '<html><body>hello world</body></html>'


@app.route('/sendprob',methods=['POST'])
def send_prob_to_app():
    output_list = ['Biking' ,' Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking']
   
    N_TIME_STEPS = 100 #sliding window length
    STEP = 50 #Sliding window step size
    N_FEATURES = 12 
    input_json = request.get_json(force=True)
    gyroscope=input_json['gyroscope']
    accelerometer=input_json['accelerometer']
    accelerometer_gravity=input_json['accelerometer_gravity']
    gyroscope=np.array(gyroscope)
    accelerometer=np.array(accelerometer)
    accelerometer_gravity=np.array(accelerometer_gravity)
    gyroscope.reshape(100,3)
    accelerometer.reshape(100,3)
    accelerometer_gravity.reshape(100,3)
    body = np.subtract(accelerometer,accelerometer_gravity)
    temp = np.hstack((accelerometer_gravity,body,gyroscope))
    df = pd.DataFrame(temp ,columns=['Ax','Ay','Az','Lx','Ly','Lz','Gx','Gy','Gz'])
    data = df
    test_X=fe.concat(data)
    test_X=fe.generate_sequence(test_X,N_TIME_STEPS, STEP)
    X_test=fe.reshape_segments(test_X,N_TIME_STEPS, N_FEATURES)
    model= keras.models.load_model('keras_model.h5')
    pred= model.predict(X_test)
    pred=pred[0].tolist()
    for i in range(0,len(pred)):
        pred[i]=round(pred[i],3)
    dictToReturn = {'output': pred}
    return jsonify(dictToReturn)

@app.route('/send',methods=['POST'])
def get_data_from_app():
    
    output_list = ['Biking' ,'Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking']
    N_TIME_STEPS = 100 #sliding window length
    STEP = 50 #Sliding window step size
    N_FEATURES = 12 
    input_json = request.get_json(force=True)
    gyroscope=input_json['gyroscope']
    accelerometer=input_json['accelerometer']
    accelerometer_gravity=input_json['accelerometer_gravity']
    gyroscope=np.array(gyroscope)
    accelerometer=np.array(accelerometer)
    accelerometer_gravity=np.array(accelerometer_gravity)
    gyroscope.reshape(100,3)
    accelerometer.reshape(100,3)
    accelerometer_gravity.reshape(100,3)
    body = np.subtract(accelerometer,accelerometer_gravity)
    temp = np.hstack((accelerometer_gravity,body,gyroscope))
    df = pd.DataFrame(temp ,columns=['Ax','Ay','Az','Lx','Ly','Lz','Gx','Gy','Gz'])
    data = df
    test_X=fe.concat(data)
    test_X=fe.generate_sequence(test_X,N_TIME_STEPS, STEP)
    X_test=fe.reshape_segments(test_X,N_TIME_STEPS, N_FEATURES)
    model= keras.models.load_model('keras_model.h5')
    pred= model.predict(X_test)
    result = predict_label(pred,output_list)
    dictToReturn = {'output': result}
    return jsonify(dictToReturn)

# @app.route('/send',methods=['POST'])
# def get_data_from_app():
#     input_json = request.get_json(force=True)
#     gyroscope=input_json['gyroscope']
#     accelerometer=input_json['accelerometer']
#     accelerometer_gravity=input_json['accelerometer_gravity']
#     gyroscope=np.array(gyroscope)
#     accelerometer=np.array(accelerometer)
#     accelerometer_gravity=np.array(accelerometer_gravity)
#     gyroscope.reshape(128,3)
#     accelerometer.reshape(128,3)
#     accelerometer_gravity.reshape(128,3)
#     body = np.subtract(accelerometer,accelerometer_gravity)
#     scaler=MinMaxScaler(feature_range=(-1,1))
#     accelerometer_gravity=scaler.fit_transform(accelerometer_gravity)
#     body=scaler.fit_transform(body)
#     gyroscope=scaler.fit_transform(gyroscope)
#     shape = list(np.array(input_json['gyroscope']).shape)
#     data= fe.extract_features(gyroscope,body,accelerometer_gravity)
#     f_2 = data
#     #loaded_model = pickle.load(open('knnpickle_file', 'rb'))
#     loaded_model = pickle.load(open('rdclfmodel.pkl', 'rb'))
#     outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
#     data = np.array(data)
#     # pred = outputlabel[int(loaded_model.predict(data.reshape(1,81)))]
#     pred=loaded_model.predict(data.reshape(1,81))
#     dictToReturn = {'data' : f_2 ,'output': pred[0],'shape':shape}
#     return jsonify(dictToReturn)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=4000,debug=True)


# def get_data_from_app():
#     N_TIME_STEPS = 100 #sliding window length
#     STEP = 50 #Sliding window step size
#     N_FEATURES = 12 
#     input_json = request.get_json(force=True) 
#     gyroscope=request.json['gyroscope']
#     accelerometer=request.json['accelerometer']
#     accelerometer_gravity=request.json['accelerometer_gravity']
#     body=np.subtract(np.array(accelerometer),np.array(accelerometer_gravity))
#     li=[accelerometer_gravity,body,gyroscope]
#     data=pd.DataFrame(data=li, columns=['Ax','Ay','Az','Lx','Ly','Lz','Gx','Gy','Gz'])
#     test_X=fe.concat(data)
#     test_X=fe.generate_sequence(test_X,N_TIME_STEPS, STEP)
#     X_test=fe.reshape_segments(test_X,N_TIME_STEPS, N_FEATURES)
#     model=keras.load_model('keras_model.h5')
#     pred=model.predict(X_test)
#     # hello=request.json['hello']
#     # shape = list(np.array(input_json['gyroscope']).shape)
#     # data= fe.extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
#     # f_2 = data
#     # #loaded_model = pickle.load(open('knnpickle_file', 'rb'))
#     # loaded_model = pickle.load(open('lrmodel (5).pkl', 'rb'))
#     # outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
#     # gxmean,gymean,gzmean=gyroscope_mean(np.array(input_json['gyroscope']))
#     # data = np.array(data)
#     # pred = outputlabel[int(loaded_model.predict(data.reshape(1,9)))]
#     # # dictToReturn = {'data' : f_2 ,'output': pred,'shape':shape,'gxmean':gxmean,'gymean':gymean,'gzmean':gzmean}
#     dictToReturn = {'output': pred}

#     return jsonify(output=dictToReturn)
#     #return jsonify(gyroscope=gyroscope,accelerometer=accelerometer)