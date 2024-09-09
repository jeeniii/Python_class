import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval

df1 = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_credits.csv')
df2 = pd.read_csv('C:\\Python\\Python_Class\\MachineLearning\\tmdb_5000\\tmdb_5000_movies.csv')

# # print(df1.head())
# # print(df1[:3])

# print(df1.shape)
# print(df2.shape)

# print(df1['title'].equals(df2['title']))
# print(df1.columns) 
# df1.columns = ['id', 'title', 'cast', 'crew']
# print(df1.columns)
# print(df2.columns)

# C = df2['vote_average'].mean()
# # print(C)
# m = df2['vote_count'].quantile(0.9)
# # print(m)

# q_movies = df2.copy().loc[df2['vote_count'] >= m ]
# print(q_movies.shape)
# q_movies['vote_count'].sort_values()
# print(q_movies['vote_count'])

# def weighted_rating(x, m=m, C=C):
#     v = x['vote_count']
#     R = x['vote_average']
#     return (v / ( v + m ) * R ) + (m / (m + v) * C)

# q_movies['score'] = q_movies.apply(weighted_rating, axis = 1)
# # print(q_movies.head(3))

# q_movies = q_movies.sort_values('score', ascending=False)
# print(q_movies[['title', 'vote_average', 'vote_count', 'score']].head(10))



# 줄거리 기반 영화 추천
tfidf = TfidfVectorizer(stop_words='english')
print(df2['overview'].isnull().values.any())
df2['overview'] = df2['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(df2['overview'])
print(tfidf_matrix.shape)

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim)
print(cosine_sim.shape)

indices = pd.Series(df2.index, index = df2['title']).drop_duplicates()
# print(indices)
print(indices['Newlyweds'])
print(df2.iloc[[4799]])

# 영화의 제목을 입력 받으면 코사인 유사도를 통해 가장 유사도가 높은 상위 10개의 영화 목록 반환
def get_recommendations(title, cosine_sim = cosine_sim):

    # 영화의 index 값 얻기
    idx = indices[title]

    # 코사인 유사도 매트릭스(cosine_sim)에서 idx에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 자기 자신을 제외한 10개의 추천 영화 슬라이싱
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)

    # 자기 자신을 제외한 10개의 추천 영화 슬라이싱
    sim_scores = sim_scores[1:11]

    #추천 영화 목록 10개의 인덱스 정보 추출
    moview_indices = [i[0] for i in sim_scores]
    
    # 인덱스 정보를 통해 영화 제목 추출
    return df2['title'].iloc[moview_indices]

# test_idx = indices['The Dark Knight Rises'] # 영화의 index 값 얻기
# print(test_idx)

# test_sim_scores = list(enumerate(cosine_sim[3]))
# print(test_sim_scores)  # 코사인 유사도 매트릭스(cosine_sim)에서 idx에 해당하는 데이터를 (idx, 유사도) 형태로 얻기

# test_sim_scores = sorted(test_sim_scores, key=lambda x:x[1], reverse=True) # reverse=True 내림차순
# print(test_sim_scores[1:11]) # 자기 자신을 제외한 10개의 추천 영화 슬라이싱


# # 람다식
# def get_second(x):
#     return x[1]

# lst = ['index', 'populate']
# print(get_second(lst))
# print('===============================')

# print((lambda x: x[1])(lst))

# #추천 영화 목록 10개의 인덱스 정보 추출
# test_moview_indices = [i[0] for i in test_sim_scores[1:11]]
# print(test_moview_indices)

# # 인덱스 정보를 통해 영화 제목 추출
# print(df2['title'].iloc[test_moview_indices])

# print(get_recommendations('Batman Forever'))

# 다양한 요소 기반 추천 (장르, 감독, 배우 등)
print(df2.columns)
# print(df1['crew'])

'''# s1 = [{"id": 28, "name": "Action"}]
# s2 = '[{"id": 28, "name": "Action"}]'

# s2 = literal_eval(s2)
# print(type(s2))

# features = ['cast', 'crew']
# for feature in features:
#     df1[feature]  = df1[feature].apply(literal_eval)
#     print(df1[feature])

# print(df1.loc[0, 'crew'])

# 감독 정보 추출
def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
        return np.nan
    
df2['director'] = df1['crew'].apply(get_director)
print(df2['director'])'''

print('Casts :',df1.loc[0, 'cast'])
print(df2.loc[0, 'genres'])
print(df2.loc[0, 'keywords'])
print('=========================================')

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > 3:
            names = names[:3]
        return names
    return []

features1 = ['cast']
for feature in features1:
    df1[feature] = df1[feature].apply(get_list)

print(df1[['cast']])

features2 = ['keywords', 'genres']
for feature in features2:
    df2[feature] = df2[feature].apply(get_list)