# HAR-backend
---

HAR-backend is API Deployed in [Heroku](https://www.heroku.com/) which gets input values from the accelerometer and gyroscope sensor of the Device and returns the output class label.

The *Model* used in the API is ***LSTM*** .

The Input values/parameter of the API is each (100 x 3) accelerometer sensor , gyroscope sensor and accelerometer due to gravity sensor values.

The API does some pre-processing before predicting the values.

The ***LSTM*** model's accuracy is 99% for the given data set.

The possible output class label from the model is ['Biking' ,'Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking'].

---





