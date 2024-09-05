import pandas as pd
import numpy as np

credits_data = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_credits.csv')
movies_data = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_movies.csv')

print(credits_data.head())
print(credits_data[:3])