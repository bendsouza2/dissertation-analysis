import pandas as pd

# Reading the data
df = pd.read_csv('binary_adjusted.csv')
df = df.set_index('company')

MAU_df = pd.read_csv('MAU.csv', header=None)
MAU_df.columns = ['company', 'MAU_millions', 'secondary_source']
MAU_df = MAU_df.set_index('company')
MAU_df['MAU_millions'] = MAU_df['MAU_millions'].astype(float)

use = pd.read_csv('use_case.csv')
use = use.set_index('company')
use = use.drop(['source', 'source_2'], axis=1).copy()
use = use.drop('user_response', axis=1).copy()
use = use.drop('share_with_third_party', axis=1).copy()
print(use)

# Aggregating the data collected by big tech companies
meta_agg = df.loc(axis=0)['facebook', 'instagram', 'whatsapp'].sum()
meta_agg.name = 'meta'
google_agg = df.loc(axis=0)['google_maps', 'youtube', 'google_docs', 'google_sheets', 'gmail'].sum()
google_agg.name = 'google'
df = df.append(meta_agg)
df = df.append(google_agg)


# Adding columns on how many categories of data companies collect
total = df.sum(axis=1)
df['total_collected'] = total


max_poss = len(df.columns) - 1
percentage = total/max_poss * 100
df['percentage'] = percentage
df['percentage'] = df['percentage'].round(decimals=2)


# Merging the two dataframes
comb = df[['percentage', 'total_collected']].merge(MAU_df, left_on='company', right_on='company')
comb = comb.drop('secondary_source', axis=1)
comb.dropna(axis=0, inplace=True)

# Correlation between MAU and data collection
monopoly_advantage = comb.corr()


# Summary statistics
companies_collecting = df.sum(axis=0)
correlation = df.corr()



