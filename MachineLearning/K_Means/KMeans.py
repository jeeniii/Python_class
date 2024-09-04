# K-Means

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\KMeansData.csv')
print(dataset[:5])

x = dataset.iloc[:, :].values
# x = dataset.to_numpy() # 공식 홈페이지 권장
print(x[:5])

# 데이터 시각화(전체 데이터 분포 확인)
# plt.scatter(x[:, 0], x[:, 1]) # x축 - hour, y축 - score
# plt.title('Score by hours')
# plt.xlabel('hour')
# plt.ylabel('scroe')

# plt.show()

# x축을 y축 범위 통일

plt.scatter(x[:, 0], x[:, 1]) # x축 - hour, y축 - score
plt.title('Score by hours')
plt.xlabel('hour')
plt.xlim(0, 100)
plt.ylabel('scroe')
plt.ylim(0, 100)

plt.show()

