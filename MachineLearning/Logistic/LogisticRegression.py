# Logistic Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\LogisticRegressionData.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)


print('6시간 공부 :', classifier.predict([[6]])) # 1= True
print('6시간 공부 합격 확률 :', classifier.predict_proba([[6]]))

print('4시간 공부 :', classifier.predict([[4]])) # 0= False
print('4시간 공부 합격 확률 :', classifier.predict_proba([[4]]))

# 분류 결과 예측
y_pred = classifier.predict(x_test)
print('분류 결과 예측 :', y_pred)

print('분류 결과 테스트 :', y_test)
print(x_test)

print('모델 평가 :',classifier.score(x_test, y_test))

# 데이터 시각화
x_range = np.arange(min(x), max(x), 0.1)
# print(x_range)
#  p = 1 / (1 + np.exp(-(m * x_range + b))) => y = mx + b
p = 1 / (1 + np.exp(-(classifier.coef_ * x_range + classifier.intercept_)))
print('예측 확률 :',p)
print(p.shape) # 2차원
print(x_range.shape) # 1차원 => 위 p.shape과 같은 차원이어야 한다.

p = p.reshape(-1)
print(p.shape) 

'''plt.scatter(x_train, y_train, color='blue') # 점
plt.plot(x_range, p, color='green') # 선
plt.plot(x_range, np.full(len(x_range), 0.5), color='red') # x_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probablilty by hours')
plt.xlabel('hours')
plt.ylabel('P')

plt.show()'''

plt.scatter(x_test, y_test, color='blue') # 점
plt.plot(x_range, p, color='green') # 선
plt.plot(x_range, np.full(len(x_range), 0.5), color='red') # x_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probablilty by hours (test)')
plt.xlabel('hours')
plt.ylabel('P')

plt.show()

print(classifier.predict_proba([[4.5]]))
print('=======================================')
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
''' 
True Negative   False Positive
불합격(예측)    합격(예측)
불합격(실제)    불합격(실제)

False Negative   True Positive
불합격(예측)    합격(예측)
합격(실제)      합격(실제)
'''