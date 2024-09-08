import pandas as pd
import numpy as np

df1 = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_credits.csv')
df2 = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_movies.csv')

# print(df1.head())
# print(df1[:3])

print(df1.shape)
print(df2.shape)

print(df1['title'].equals(df2['title']))
print(df1.columns) 
df1.columns = ['id', 'title', 'cast', 'crew']
print(df1.columns)
print(df2.columns)

C = df2['vote_average'].mean()
# print(C)
m = df2['vote_count'].quantile(0.9)
# print(m)

q_movies = df2.copy().loc[df2['vote_count'] >= m ]
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