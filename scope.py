import pandas as pd

# pd.set_option('display.max_columns', 100)

eos = pd.read_csv('economies_scope.csv')
eos = eos.drop('Product Market', axis=1)

a = list(eos.columns)
maxi = len(eos['google_search'])

c = eos.isin(['0']).sum(axis=0)

f = list(c)
semi = {'company': a, 'zeroes': f}
final_eos = pd.DataFrame(semi)
final_eos.set_index('company', inplace=True)
final_eos['non_zero'] = maxi - final_eos['zeroes']
print(final_eos)
