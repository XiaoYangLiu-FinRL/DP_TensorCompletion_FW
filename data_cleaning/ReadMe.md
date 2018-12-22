# 文件结构

```
|- jester1.py           # Jester dataset1 处理代码
|- movielens_10m_top_400.py     # Movielens_10M 处理代码
|- netflix_top_400_id.py        # Netflix(step1): get top 400
|- netflix_top_400_result.py    # Netflix(step2): deal with top 400
|- ...
|- jester1_rating_data_treated.xlsx     # 数据清洗结果: Jester Dataset1
|- movielens_10m_top_400.xlsx           #               MovieLens_10M Top-400
|- netflix_top_400_result.csv           #               Netflix Top-400
|- ...
|- data/                # 原始数据集
    |- jester1              # Get from http://eigentaste.berkeley.edu/dataset/
        |- jester-data-1.xls
        |- jester-data-2.xls
        |- jester-data-3.xls
    |- movielens            # Get from https://grouplens.org/datasets/movielens/
        |- ml-10m/ml10M100K
            |- movies.dat
            |- ratings.dat
            |- ...
    |- netflix              # Get from http://academictorrents.com/details/9b13183dc4d60676b773c9e2cd6de5e5542cee9a
        |- movie_titles.txt
        |- training_set
            |- mv_0000001.txt
            |- mv_0000002.txt
            |- ...
            |- mv_0017770.txt
    |- YahooMusic           # Get from https://webscope.sandbox.yahoo.com/catalog.php?datatype=c
```

# Jester

- 原始数据 (Jester Dataset 1)
    * 下载地址 <http://eigentaste.berkeley.edu/dataset/>
    * 100 个笑话(joke), 73421 个用户(user)，超过 4.1 million 评分(rating)
    * Rating 范围 (-10.0, 10.0)
    * 未评分 (not rated) 条目插入 99
    * 每行代表一个用户，每行第一列代表该用户的评分数量！！！
- 处理后数据 (jester1_rating_data_treated.xlsx)
    * size: 73421 x 100
    * 每行代表一个用户的 rating
    * Rating 由原始数据的 (-10.0, 10.0) 调整到 (0, 5) 区间
        - rating = (rating + 10) / 20 * 5
    * Not Rating 插入 99

# MovieLens

- 原始数据 (MovieLens 10M)
    * 下载地址 <https://grouplens.org/datasets/movielens/>
    * 结构比较简单，详见数据集的 README.html
- 处理后数据 (movielens_10m_top_400.xlsx)
    * size: 69878 x 400
    * 每行代表一个用户的 rating
    * Rating 范围: (0, 5)
    * Not Rating 为 0
        - 官网未发现 Not Rating 值的说明，从此处得知 <https://webpages.uncc.edu/paraball/>

# Netflix

- 原始数据
    * 下载地址 <http://academictorrents.com/details/9b13183dc4d60676b773c9e2cd6de5e5542cee9a>
    * movie_titles.txt 文件存储了 MovieID:YearOfRelease:Title
    * training_set/ 目录中是电影的评分数据，每个文件存储一部电影的 CustomerID:Rating:Date 数据，共有 17770 个文件
    * Rating 范围: (1, 5)
    * Not Rating: 每个电影的 Rating 数据单独给出，且都明确对应到了每个用户，不存在 Not Rating 混淆的问题
- 处理后数据 (netflix_top_400_result.csv)
    * Netflix 数据集比较大，分了两步处理
        1. netflix_top_400_id.py (计算每个电影 rating 文件中的评分条数，排序找出 Rating-Top-400 的电影，
          记录到 netflix_top_400_id.xlsx 文件)
        2. netflix_top_400_rating.py (根据上一步的结果，读入 Top-400 的 rating 数据，最后处理输出到
          netflix_top_400_result.csv 文件，下面说明该文件内容)
    * size: 474332 x 400
    * 每行代表一个用户的 rating
    * Rating 范围: (1, 5)
    * Not Rating 为 0

# Yahoo Music

TODO:
