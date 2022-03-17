import itertools
import pandas as pd

pd.set_option('display.max_columns', 100)
use = pd.read_csv('use_case.csv')
use = use.set_index('company')
use = use.drop(['source', 'source_2'], axis=1).copy()
use = use.drop('user_response', axis=1).copy()
use = use.drop('share_with_third_party', axis=1).copy()


# Aggregating the use case of big tech companies
meta_agg = use.loc(axis=0)['facebook', 'instagram', 'whatsapp'].sum()
meta_agg.name = 'meta'
google_agg = use.loc(axis=0)['google_maps', 'youtube', 'google_docs', 'google_sheets', 'gmail'].sum()
google_agg.name = 'google'
amazon_agg = use.loc(axis=0)['amazon', 'alexa', 'prime', 'twitch'].sum()
amazon_agg.name = 'amazon_agg'
microsoft_agg = use.loc(axis=0)['bing', 'edge_ie', 'windows'].sum()
microsoft_agg.name = 'microsoft'
apple_agg = use.loc(axis=0)['apple_ios', 'safari', 'apple_tv'].sum()
apple_agg.name = 'apple'
use = use.append(meta_agg)
use = use.append(google_agg)
use = use.append(amazon_agg)
use = use.append(microsoft_agg)
use = use.append(apple_agg)


big_tech = ['amazon_agg', 'meta', 'google', 'microsoft', 'apple']
ms = ['edge_ie', 'windows']  # keeping Bing
ap = ['safari', 'apple_tv']  # keeping apple_ios
al = ['google_maps', 'youtube', 'google_docs', 'google_sheets', 'gmail']  # keeping android
am = ['alexa', 'prime', 'twitch']  # keeping amazon
me = ['instagram', 'whatsapp']  # keeping facebook
tech_to_remove = itertools.chain(ms, ap, al, am, me)
tech_to_remove = list(tech_to_remove)
non_tech = ['lidl_plus', 'ikea_app', 'pornhub', 'wetherspoon', 'cvs_pharmacy', 'costar', 'slimming_world',
            'american_airlines', 'tesco']

table_2 = use.copy()
table_2 = table_2.drop(tech_to_remove, axis=0)
table_2 = table_2.drop(non_tech, axis=0)
table_2 = table_2.drop(big_tech, axis=0)

# Formatting as Big Tech
table_2 = table_2.rename(index={'bing': 'Microsoft'})
table_2 = table_2.rename(index={'android': 'Alphabet'})
table_2 = table_2.rename(index={'apple_ios': 'Apple'})
table_2 = table_2.rename(index={'amazon': 'Amazon'})
table_2 = table_2.rename(index={'facebook': 'Meta'})

# Formatting non Big Tech
bt = ['Alphabet', 'Amazon', 'Apple', 'Meta', 'Microsoft']
non_bt = []
for i, row in table_2.iterrows():
    if i not in bt:
        non_bt.append(i)

others = table_2.loc(axis=0)[non_bt].sum()
total_others = len(non_bt)
percent = others/total_others * 100
percent.name = 'Percent'
table_2 = table_2.append(percent)
table_2 = table_2.round(decimals=2)
table_2.drop(non_bt, inplace=True)
table_2.to_csv('table2.csv')