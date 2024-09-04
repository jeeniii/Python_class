# Multi Linear Regression 다중 선형 회귀

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\MultipleLinearRegressionData.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# print(x, y)

# ColumnTransformer(transformers=[('Name', OneHotEncoder(), ["col1", "col2"])]) 
# drop = 'first' : 3개가 있으면 2개만 쓰고 10개면 9개만 사용
# remainder = 'passthrough' 인코딩하지 않은 컬럼은 놔둔다
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop = 'first'), [2])], remainder = 'passthrough')
x = ct.fit_transform(x)
# print(x)

''' 
1 0 : Home
0 1 : Library
0 0 : Cafe
'''

# 데이터 세트 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

reg = LinearRegression()
reg.fit(x_train, y_train)

# 예측 값, 실제 값 비교
y_pred = reg.predict(x_test)
print(y_pred)
print(y_test)
print(reg.coef_)
print(reg.intercept_)

# 모델 평가
print(reg.score(x_train, y_train))
print(reg.score(x_test, y_test))
print('===============================')

# 평가 지표
# MAE(Mean Absolute Error) : (실제 값과 예측 값) 차이의 절대값
# MSE(Mean Squared Error) : 차이의 제곱
# RMAE(Root Mean Squared Error) : 차이의 제곱에 루트
# R2 : 결정 계수
# => R2는 1에 가까울 수록, 나머지는 0에 가까울 수록 좋음

print('MAE :', mean_absolute_error(y_test, y_pred)) # 실제값, 예측 값
print('MSE :', mean_squared_error(y_test, y_pred))
print('RMAE :', mean_squared_error(y_test, y_pred, squared=False))
print('R2 :', r2_score(y_test, y_pred))
