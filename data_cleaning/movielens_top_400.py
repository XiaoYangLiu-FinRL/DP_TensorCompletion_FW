# coding=UTF-8

import pandas as pd

# #定义用户表的列名称
# unames = ['user_id', 'gender', 'age','occupation', 'zip']
# #读的时候注意标分隔符为::，且没有表头，故用我们自己定义的表头
# users = pd.read_table('users.dat', sep = '::', header=None, names=unames)
# 同样的方法导入电影数据表、电影评分表
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('./data/movielens/ml-10m/ml-10M100K/ratings.dat',
                        sep='::', header=None, names=rating_names)
movie_names = ['movie_id', 'title', 'genres']
movies = pd.read_table('./data/movielens/ml-10m/ml-10M100K/movies.dat',
                       sep='::', header=None, names=movie_names)

# 合并users、users、movies表
# data = pd.merge(pd.merge(users, ratings), movies)
data = pd.merge(movies, ratings)

ratings_by_title = data.groupby('title').size()

chosen = ratings_by_title.sort_values(ascending=False).head(400).index

target = data.pivot_table(values='rating',index='title',columns='user_id',)
target = target.fillna(0)
target = target.loc[chosen]
target = target.T
target.to_excel('movielens_10m_top_400.xlsx', 'sheet1')

