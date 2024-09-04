# 1. Linear Regression
# 공부 시간에 따른 시험 점수

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\LinearRegressionData.csv')
dataset.head() # head - 상위 5개만 보임

'''
[:, :-1] => ':' 모든 행, ':-1' 처음부터 마지막 컬럼 직전까지의 모든 열, -1은 마지막 열
ex)
A	B	C
1	4	7
2	5	8
3	6	9

dataset.iloc[:, :-1]
[[1, 4],
 [2, 5],
 [3, 6]]

dataset.iloc[:, -1]
[7, 8, 9]
'''
x = dataset.iloc[:, :-1].values # 처음부터 마지막 컬럼 직전까지의 데이터 (독립 변수)
y = dataset.iloc[:, -1].values # 모든 행(:)과 마지막 열(-1)
# print(x)
# print(y)

reg = LinearRegression() # 객체 생성
reg.fit(x,y) #학습 (모델 생성)
y_pred = reg.predict(x)
# print(y_pred) # 시간 별 예측 점수 출력( 0.5, 1.2, 1.8, ...)
# 예측 점수 식
#  y = mx + b   , m : (기울기), b : (y 절편)

plt.scatter(x, y, color='blue') # 산점도 그래프 (주어진 x,y데이터)
plt.plot(x, y_pred, color='green') # 선 그래프 (x와 y예측치)
plt.title('Score by hours') # 제목
plt.xlabel('hour') # X 축
plt.ylabel('score') # Y 축

# plt.show()
print('9,8,7시간 공부했을 때 예상 점수 : ', reg.predict([[9], [8], [7]]))

print(reg.coef_) # 기울기

print(reg.intercept_) # y 절편
