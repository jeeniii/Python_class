# Polynomial Regression 다항회귀
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\PolynomialRegressionData.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Simple Line Reg
reg = LinearRegression()
reg.fit(x,y)

# plt.scatter(x, y, color='blue')
# plt.plot(x, reg.predict(x), color='green')
# plt.title('Score by Hours(genius)')
# plt.xlabel('hours')
# plt.ylabel('score')

# plt.show()

# print(reg.coef_)

# Polynomial Reg
poly_reg = PolynomialFeatures(degree = 4) # degree=2 : 2차 방정식
x_poly = poly_reg.fit_transform(x)
# print('x :',x[:5])
# print('x_poly :', x_poly[:5]) # [x]-> [x^0, x^1, x^2] -> x가 3이라면 [1,3,9] 로 변환

print(poly_reg.get_feature_names_out())

line_reg = LinearRegression()
line_reg.fit(x_poly, y) #변환된 x와 y를 가지고 모델 생성

# plt.scatter(x, y, color='blue')
# plt.plot(x, line_reg.predict(poly_reg.fit_transform(x)), color='green')
# plt.title('Score by Hours')
# plt.xlabel('hours')
# plt.ylabel('score')
# plt.show()

x_range = np.arange(min(x), max(x), 0.1) #x의 최소~최대값까지의 범위를 0.1 단위로 잘라서 데이터 생성
# print(x_range)
x_range = x_range.reshape(-1, 1) #row 개수는 자동으로 계산, column 개수는 1개
# print(x.shape)
# print(x_range.shape)

plt.scatter(x, y, color='blue')
plt.plot(x_range, line_reg.predict(poly_reg.fit_transform(x_range)), color='green')
plt.title('Score by Hours(Change Range)')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

# 성적 예측
print(reg.predict([[2]])) # 2시간 공부 시 선형 회귀 모델 예측
print(line_reg.predict(poly_reg.fit_transform([[2]]))) # 2시간 공부 시 다항 회귀 모델 예측

print(line_reg.score(x_poly, y)) # 모델 평가