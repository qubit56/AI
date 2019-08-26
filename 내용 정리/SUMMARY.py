from keras.models import Sequential
from keras.layers import Dropout, Flatten, BatchNormalization, Dense, LSTM, Conv2D 
from keras import regularizers
import numpy as np
import tensorflow as tf

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Dataset Loading ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
x_train = []
y_train = []
x_test = []
y_test = []

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Data Splitting ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split     (
    x, y, random_state=0, train_size=0.8, test_size=0.2 )

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ to_categorical ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Design ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
model = Sequential()
model.add(( , input_shape=(), activation=''))
model.add(Dropout())
model.add(Flatten())
model.add(BatchNormalization())
model.add(())

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Compile ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
model.compile(optimizer='', loss='', metrics=[''])

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Fit ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=128, mode='auto')

model.fit(x_train, y_train, epochs=128, batch_size=128,
          callbacks=[early_stopping], validation_data=(x_val, y_val))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Evaluate&Predict ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
loss, acc = model.evaluate(x_test, y_test, batch_size=128)

y_predict = model.predict(x_test)
print(y_predict)

# RMSE solution
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

# R2 solution
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)
