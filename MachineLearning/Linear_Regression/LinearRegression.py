# 1. Linear Regression
# 공부 시간에 따른 시험 점수

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('LinearRegressionData.csv')
dataset.head() # head - 상위 5개만 보임
print(dataset.head())
