import pandas as pd
import numpy as np

credits_data = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_credits.csv')
movies_data = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_movies.csv')

# print(credits_data.head())
# print(credits_data[:3])

print(credits_data.shape)
print(movies_data.shape)

print(credits_data['title'].equals(movies_data['title']))
print(credits_data.columns) 
credits_data.columns = ['id', 'title', 'cast', 'crew']
print(credits_data.columns) 