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
print(movies_data.columns)

C = movies_data['vote_average'].mean()
# print(C)
m = movies_data['vote_count'].quantile(0.9)
# print(m)

q_movies = movies_data.copy().loc[movies_data['vote_count'] >= m ]
print(q_movies.shape)
q_movies['vote_count'].sort_values()
print(q_movies['vote_count'])

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / ( v + m ) * R ) + (m / (m + v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis = 1)
# print(q_movies.head(3))

q_movies = q_movies.sort_values('score', ascending=False)
print(q_movies[['title', 'vote_average', 'vote_count', 'score']].head(10))