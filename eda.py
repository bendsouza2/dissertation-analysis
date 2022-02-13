import pandas as pd

# Reading the data
df = pd.read_csv('binary_data.csv')
df = df.set_index('company')


# Adding columns on how many categories of data companies collect
total = df.sum(axis=1)
df['total_collected'] = total

max_poss = len(df.columns) - 1
percentage = total/max_poss * 100
df['percentage'] = percentage
df['percentage'] = df['percentage'].round(decimals=2)
print(df.head())

# Summary statistics
companies_collecting = df.sum(axis=0)
print(companies_collecting)
correlation = df.corr()
print(correlation.between(0.7, 0.999))

