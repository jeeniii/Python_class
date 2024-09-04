import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\LinearRegressionData.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0) #훈련 80: 테스트 20 으로 분리
# print(x, len(x))
# print(x_train, len(x_train))
# print(x_test, len(x_test))

# print(y, len(y))
# print(y_train, len(y_train))
# print(y_test, len(y_test))


# 분리된 데이터로 모델링
reg = LinearRegression()
reg.fit(x_train, y_train) # fit - 훈련


# 데이터 시각화 (Training Set)
plt.scatter(x_train, y_train, color='blue')
plt.plot(x_train, reg.predict(x_train), color='green')
plt.title('Training Set')
plt.xlabel('hour')
plt.ylabel('score')

# plt.show()

# 데이터 시각화 (Training Set)
plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, reg.predict(x_test), color='green')
plt.title('Test Set')
plt.xlabel('hour')
plt.ylabel('score')

# plt.show()

print(reg.coef_) # 기울기
print(reg.intercept_) # y 절편

# 모델 평가
print(reg.score(x_test, y_test)) #테스트 세트로 모델 평가
print(reg.score(x_train, y_train)) #훈련 세트로 모델 평가



