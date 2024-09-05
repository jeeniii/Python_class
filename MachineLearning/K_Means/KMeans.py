# K-Means

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

dataset = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\csv_file\\KMeansData.csv')
print(dataset[:5])

x = dataset.iloc[:, :].values
# x = dataset.to_numpy() # 공식 홈페이지 권장
print(x[:5])

# 데이터 시각화(전체 데이터 분포 확인)
# plt.scatter(x[:, 0], x[:, 1]) # x축 - hour, y축 - score
# plt.title('Score by hours')
# plt.xlabel('hour')
# plt.ylabel('score')

# plt.show()

# x축을 y축 범위 통일

# plt.scatter(x[:, 0], x[:, 1]) # x축 - hour, y축 - score
# plt.title('Score by hours')
# plt.xlabel('hour')
# plt.xlim(0, 100)
# plt.ylabel('score')
# plt.ylim(0, 100)

# plt.show()

sc = StandardScaler()
x = sc.fit_transform(x)
print(x[:5])

# 스케일링 데이터
plt.figure(figsize=(5,5))
plt.scatter(x[:, 0], x[:, 1]) # x축 - hour, y축 - score
plt.title('Score by hours')
plt.xlabel('hour')
plt.ylabel('score')

plt.show()

# 최적 K 찾기 (Elbow Method)
inertia_list = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(x)
    inertia_list.append(kmeans.inertia_) # 각 지점으로부터 클러스터의 중심까지의 거리의 제곱의 합

plt.plot(range(1,11), inertia_list)
plt.title('Elbow Method')
plt.xlabel('n_clusters')
plt.ylabel('inertia')

plt.show()

# 최적의 k(4) 값으로  KMeans 학습
K = 4
kmeans = KMeans(n_clusters = K, random_state = 0)
y_kmeans = kmeans.fit_predict(x)
print(y_kmeans)

centers = kmeans.cluster_centers_
print(centers)

for cluster in range(K):
    plt.scatter(x[y_kmeans == cluster, 0], x[y_kmeans == cluster, 1], s = 100, edgecolors='black')
    plt.scatter(centers[cluster, 0], centers[cluster, 1], s = 300, edgecolors='yellow', marker='s')
    plt.text(centers[cluster, 0], centers[cluster, 1], cluster, va='center', ha = 'center')

plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')

plt.show()

# 데이터 시각화 (스케일링 원복)
x_org = sc.inverse_transform(x)
print(x_org[:5])

centers_org = sc.inverse_transform(centers)
print(centers_org)

for cluster in range(K):
    plt.scatter(x_org[y_kmeans == cluster, 0], x_org[y_kmeans == cluster, 1], s = 100, edgecolors='black')
    plt.scatter(centers_org[cluster, 0], centers_org[cluster, 1], s = 300, edgecolors='yellow', marker='s')
    plt.text(centers_org[cluster, 0], centers_org[cluster, 1], cluster, va='center', ha = 'center')

plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')

plt.show()