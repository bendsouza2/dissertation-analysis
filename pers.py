import pandas as pd

initial = pd.read_csv('pd_final.csv')

# Adding column of how many categories of data each company collects
total = initial.sum(axis=1)
initial['total_collected'] = total
maxi = len(initial.columns)
percentage = total/maxi * 100
initial['percentage_collected'] = percentage.round(decimals=2)
print(initial)

