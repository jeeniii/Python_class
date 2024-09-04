# Gradient Descent

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor # Stochastic Gradient Descent: 확률적 경사하강법

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\LinearRegressionData.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0) #훈련 80: 테스트 20 으로 분리

# max_iter : 훈련 세트 반복 횟수 (Epoch 횟수) => max_iter를 변경할 경우 기울기가 변화된다 100, 200, 300, ...
# eta0 : 학습률 (learning rate)
'''지수 표기법
1e-3 : 0.001(10^-3)
1e-4 : 0.0001(10^-4)
1e+3 : 1000(10^3)
1e+4 : 10000(10^4)
'''
sr = SGDRegressor(max_iter=1000, eta0=1e-4, random_state=0, verbose=1)
sr.fit(x_train, y_train)

plt.scatter(x_train, y_train, color='blue')
plt.plot(x_train, sr.predict(x_train), color='green')
plt.title('Stochastic Gradient Descent')
plt.xlabel('hour')
plt.ylabel('score')
plt.show()

# print(sr.coef_, sr.intercept_)

# print(sr.score(x_test, y_test))
# print(sr.score(x_train, y_train))