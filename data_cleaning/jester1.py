########################################################################################################################
# Input:    ./data/jester1/jester-data-1.xls
#           ./data/jester1/jester-data-2.xls
#           ./data/jester1/jester-data-2.xls
# Output:   ./jester1_rating_data_treated.xlsx
########################################################################################################################
import pandas as pd
from pandas import DataFrame

# Read original data
print('Read raw data.')
jester1_data_part1 = pd.read_excel('./data/jester1/jester-data-1.xls',
                                   sheet_name='jester-data-1-new', header=None)
jester1_data_part2 = pd.read_excel('./data/jester1/jester-data-2.xls',
                                   sheet_name='jester-data-2-new', header=None)
jester1_data_part3 = pd.read_excel('./data/jester1/jester-data-3.xls',
                                   sheet_name='jester-data-3-new', header=None)

# Merge data
print('Merge data.')
jester1_data = jester1_data_part1
jester1_data = jester1_data.append(jester1_data_part2)
jester1_data = jester1_data.append(jester1_data_part3)
# DataFrame(jester1_data).to_excel("jester1-data-merge.xlsx", sheet_name="Sheet1",
#                                  index=False, header=False)

# 1. Rating movie count by exactly person
#    from the first column
print('Export rating count by person.')
jester1_rating_count_by_person = jester1_data[[0]]
DataFrame(jester1_data).to_excel("jester1_rating_count_by_person.xlsx",
                                 sheet_name="Sheet1", index=False, header=False)

# 2. Rating data for 100 movies
#    from the rest 100 columns
print('Get rating data')
sel = (sel+1 for sel in range(100))
jester1_rating_data = DataFrame(jester1_data, columns=sel)
# DataFrame(jester1_data).to_excel("jester1_rating_data.xlsx",
#                                  sheet_name="Sheet1", index=False, header=False)

# Separate valid & invalid(99) rating data
valid_rating = jester1_rating_data[jester1_rating_data < 99]
valid_rating.fillna(0, inplace=True)
# DataFrame(valid_rating).to_excel("valid_rating.xlsx",
#                                  sheet_name="Sheet1", index=False, header=False)
invalid_rating = jester1_rating_data[jester1_rating_data >= 99]
invalid_rating.fillna(0, inplace=True)
# DataFrame(invalid_rating).to_excel("invalid_rating.xlsx",
#                                    sheet_name="Sheet1", index=False, header=False)

# Normalization
# [-10, 10]  -->> [0, 5]
print('Normalization.( [-10,10] -->> [0,5] )')
valid_rating = (valid_rating + 10)/20*5

# Fill not-rating section(with 99)
valid_rating[invalid_rating >= 99] = 99

# Result
print('Output rating data...')
DataFrame(valid_rating).to_excel("jester1_rating_data_treated.xlsx",
                                 sheet_name="Sheet1", index=False, header=False)

print('Done')
