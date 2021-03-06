# 1 ~ 100까지의 숫자를 이용해서 6개씩 잘라서 RNN 구성
# train, test로 분리

# 1, 2, 3, 4, 5, 6 : 7
# 2, 3, 4, 5, 6, 7 : 8
# 3, 4, 5, 6, 7, 8 : 9
# ...
# 94, 95, 96, 97, 98, 99 : 100

# predict 101 ~ 110까지 예측하시오.
# 지표 RMSE

from keras.models import Sequential
from keras.layers import Dropout, Flatten, BatchNormalization, Dense, LSTM
import numpy as np

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Dataset Loading ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
arraySet = np.array(range(1, 101))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Data Splitting ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
size = 7
def split_n(seq, size):
    newList = []
    for i in range(len(seq) - size + 1):
        subset = seq[i:(i+size)]
        newList.append([item for item in subset])
    # print(type(newList))
    return np.array(newList)

dataset = split_n(arraySet, size)
# print(dataset)
# print(dataset.shape)    # (94, 7)
x_data = dataset[:, :6] #(6)
y_data = dataset[:, -1] #(6, )
# print(x_data, "\n", y_data)
# print(x_data.shape, y_data.shape)   # (94, 6) (94,)
y_data = y_data.reshape(-1, 1)
# print(y_data.shape)   # (94, 1)

# x_data = x_data.reshape(1, 94, 6)
# y_data = y_data.reshape(1, 94, 1)
# print(x_data.shape, y_data.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, train_size=0.8, random_state=66
)
# print(x_train.shape, x_test.shape)  # (75, 6) (19, 6)
# print(y_train.shape, y_test.shape)  # (75, 1) (19, 1)

x_train = x_train.reshape(-1, 1, 6)
x_test = x_test.reshape(-1, 1, 6)
# print(x_train.shape, x_test.shape)  # (75, 1, 6) (19, 1, 6)
# print(x_train, "\n", x_test)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Design ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
model = Sequential()

model.add(LSTM(32, input_shape=(1, 6), activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Compile ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Fit ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
model.fit(x_train, y_train, epochs=100, batch_size=1)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Model Evaluate&Predict ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
loss, acc = model.evaluate(x_test, y_test, batch_size=1)
print("Accuracy: ", acc)

# y_predict = model.predict(x_test)
# print(y_predict)    # 19개 출력

x_test = np.array(range(95, 111))
x_test = split_n(x_test, 7)
x_test = x_test[:, :6]
x_test = x_test.reshape(-1, 1, 6)

y_predict = model.predict(x_test, verbose=1)
print(y_predict)

y_test = np.array(range(101, 111))
y_test = y_test.reshape(10, 1)

# RMSE solution
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))
