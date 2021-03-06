import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#1. 데이터
a = np.array(range(1,11))

size = 5
def split_5(seq, size):
    aaa = []
    for i in range(len(seq) - size + 1): # i= 0~5 6줗
        subset = seq[i:(i+size)] # 0~5 : 4~9 1줄씩
        aaa.append([item for item in subset])
    # print(type(aaa))
    return np.array(aaa)

dataset = split_5(a, size)
print(dataset)
x_train = dataset[:, 0:4] #(6,4)
y_train = dataset[:, 4, ] #(6, )

print("====================")
# print(x_train.shape)
# print(y_train.shape)
print(x_train)
print(y_train)

scaler = StandardScaler()
# scaler = MinMaxScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
print(x_train_scaled)

# x_test_scaled = scaler.transform(x_test)

# print(x_train_scaled)


x_train = np.reshape(x_train, (len(a) - size + 1, 4, 1))

print(x_train.shape)

x_test = np.array([[[11],[12],[13],[14]], [[12],[13],[14],[15]],
                   [[13],[14],[15],[16]], [[14],[15],[16],[17]]])

y_test = np.array([15,16,17,18])


print(x_test.shape)
print(y_test.shape)

# x = x.reshape((x.shape[0], x.shape[1], 1))
# print("x.shape : ", x.shape)


'''
#2. 모델 구성
model = Sequential()

model.add(LSTM(32, input_shape=(4,1), return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10, return_sequences=True))
model.add(LSTM(10))

model.add(Dense(5, activation='relu'))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(1))

model.summary()

#3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=30, mode='auto')

model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1,
          callbacks=[early_stopping])

loss, acc = model.evaluate(x_test, y_test)

y_predict = model.predict(x_test)

print('loss : ', loss)
print('acc : ', acc)
print('y_predict(x_test) : \n', y_predict)
'''