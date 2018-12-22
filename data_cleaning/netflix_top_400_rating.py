# you need run 'netflix_find_top_400.py' first
import pandas as pd

netflix_data_dir = './data/netflix/'
training_data_dir = netflix_data_dir + 'training_set/'

input_file = './netflix_top_400_id.xlsx'

movie_rating_names = ['MovieID', 'RatingCount']
movie_top_400 = pd.read_excel(input_file, sheet_name='Sheet1', names=movie_rating_names)
movie_id = movie_top_400['MovieID']

rating_names = ['CustomerID', 'Rating', 'Date']
rating_by_movies = pd.DataFrame()
for i in range(400):
    rating_file = training_data_dir + 'mv_{0:07d}.txt'.format(movie_id[i])
    rating = pd.read_table(rating_file, sep=',', header=None, names=rating_names)
    rating_temp = rating.iloc[1:, :]
    rating_temp.insert(0, 'MovieID', movie_id[i])
    rating_by_movies = rating_by_movies.append(rating_temp)
    print('{0:7d}'.format(i))

# Merge
print('Merge')
data = pd.merge(movie_top_400, rating_by_movies)
print('group by')
rating_in_order_size = data.groupby('MovieID').size()

# print('sort')
# chosen = rating_in_order_size.sort_values(ascending=False).head(400).index
print('process')
target = data.pivot_table(values='Rating', index='MovieID', columns='CustomerID')
target = target.fillna(0)
# target = target.loc[chosen]
target = target.T
print('save')
target.to_csv('netflix_top_400_result.csv')
print('Done')
