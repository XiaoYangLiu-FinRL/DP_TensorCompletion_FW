import pandas as pd

netflix_data_dir = './data/netflix/'
training_data_dir = netflix_data_dir + 'training_set/'
movie_num = 17770
# movie_num = 100

# Movies
# movie_names = ['MovieID', 'YearOfRelease', 'Title']
# movie_title_file = netflix_data_dir + 'movie_titles.txt'
# movies = pd.read_table(movie_title_file, sep=',', header=None, names=movie_names)

# Ratings
rating_names = ['CustomerID', 'Rating', 'Date']
# rating_by_movies = pd.DataFrame()
movie_rating_count = []
for i in range(movie_num):
    index = i+1
    rating_file = training_data_dir + 'mv_{0:07d}.txt'.format(index)
    rating = pd.read_table(rating_file, sep=',', header=None, names=rating_names)
    movie_rating_count.append([index, len(rating)-1])
    # rating_temp = rating.iloc[1:, 0:2]
    # rating_temp.insert(0, 'MovieID', index)
    # rating_by_movies = rating_by_movies.append(rating_temp)
    if not (index % 100):
        print('{0} files has been read...'.format(index))

print('all files loaded.')

# Find Top 400
print('Find top 400...')
movie_rating_count.sort(key=lambda x: x[1], reverse=True)
movie_top_400 = movie_rating_count[:400]
df_move_rating_count = pd.DataFrame(movie_top_400, columns=['MovieID', 'RatingCount'])

# Save Result
print('Export top 400 to excel...')
df_move_rating_count.to_excel('netflix_top_400_id.xlsx', 'Sheet1', index=False)

print('Done')

# # Merge
# print('Merge')
# data = pd.merge(movies, rating_by_movies)
# print('group by')
# rating_in_order_size = data.groupby('MovieID').size()
#
# print('sort')
# chosen = rating_in_order_size.sort_values(ascending=False).head(400).index
# print('process')
# target = data.pivot_table(values='Rating', index='MovieID', columns='CustomerID',)
# target = target.fillna(0)
# target = target.loc[chosen]
# target = target.T
# print('save')
# target.to_excel('netflix_top_400.xlsx', 'sheet1')
# print('Done')
