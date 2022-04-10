import pandas as pd

# pd.set_option('display.max_columns', 100)
initial = pd.read_csv('pd_final.csv')

# Removing unnecessary columns
unnecessary = ['marital_status', 'height', 'weight', 'next_of_kin', 'mum_maiden_name', 'birth_country',
               'allergies']
initial.drop(unnecessary, inplace=True, axis=1)

# Merging columns where categories overlap
initial.loc[initial['job'] == 1, 'employment_status'] = 1
initial.loc[initial['employer'] == 1, 'employment_status'] = 1
initial.loc[initial['past_employer'] == 1, 'employment_status'] = 1
extra_job = ['job', 'employer', 'past_employer']
initial.drop(extra_job, axis=1, inplace=True)
initial.loc[initial['social_profile_friends'] == 1, 'social_profile_interests'] = 1
initial.loc[initial['social_profile_hobbies'] == 1, 'social_profile_interests'] = 1
extra_social = ['social_profile_hobbies', 'social_profile_friends']
initial.drop(extra_social, axis=1, inplace=True)

# Adding column of how many categories of data each company collects
total = initial.sum(axis=1)
initial['total_collected'] = total
maxi = len(initial.columns)
percentage = total/maxi * 100
initial['percentage_collected'] = percentage.round(decimals=2)
print(initial.head(2))

initial.to_csv('final_personal_data.csv')

