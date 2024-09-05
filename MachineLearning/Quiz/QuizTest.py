import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\QuizData.csv')
# print(dataset)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

reg = LinearRegression()

# 학습
reg.fit(x_train, y_train)

# print('x_train :',x_train)
# print('y_train :',y_train)

# 학습 시킨 데이터로 예측 값 가져오기
y_pred_train = reg.predict(x_train)
y_pred_test = reg.predict(x_test)
# print(y_pred)

# traning 시각화
plt.scatter(x_train, y_train, color='blue') # 훈련 데이터 점
plt.plot(x_train, reg.predict(x_train), color='yellow') # 예측 데이터 선
plt.title('Quiz Train')
plt.xlabel('total')
plt.ylabel('reception')

plt.show()

# test 시각화
plt.scatter(x_test, y_test, color='blue') # 테스트 데이터 점
plt.plot(x_train, reg.predict(x_train), color='yellow') # 예측 데이터 선
plt.plot(x_test, reg.predict(x_test), color='red') # 예측 데이터 선
plt.title('Quiz Test')
plt.xlabel('total')
plt.ylabel('reception')

plt.show()

print('==============================================')
print(reg.coef_)
print(reg.intercept_)

print(reg.score(x_train, y_train))
print(reg.score(x_test, y_test))

total = 300
rept =  reg.predict([[total]])
print(rept) # 소수점으로 출력 됨
print(np.around(rept))
print(int(np.around(rept))) # Deprecated
print(np.around(rept).astype(int)) 