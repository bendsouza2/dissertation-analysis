import pandas as pd

# Reading the data
df = pd.read_csv('binary_data.csv')
df = df.set_index('company')


# Adding columns on how many categories of data companies collect
total = df.sum(axis=1)
df['total_collected'] = total
print(df)

# Aggregating the data collected by big tech companies
meta_agg = df.loc(axis=0)['facebook', 'instagram', 'whatsapp'].sum()
meta_agg.name = 'meta'
google_agg = df.loc(axis=0)['google_maps', 'youtube', 'google_docs', 'google_sheets', 'gmail'].sum()
google_agg.name = 'google'
df = df.append(meta_agg)
df = df.append(google_agg)
print(df)

max_poss = len(df.columns) - 1
percentage = total/max_poss * 100
df['percentage'] = percentage
df['percentage'] = df['percentage'].round(decimals=2)
print(df.head())

# Summary statistics
companies_collecting = df.sum(axis=0)
print(companies_collecting)
correlation = df.corr()



