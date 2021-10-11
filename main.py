# Jeremy Lee
#
# Goal/Prompt:
#
# Coding Challenge #1: For each State that we operate in, on which [week_ending] did the average of our healthcare
# personal with a completed vaccination exceed 80%?
#
# Coding Challenge #2: For each of Our Providers, what is their longest streak (# of weeks) of residents not testing
# positive for Covid-19 ([residents_weekly_confirmed_covid_19])?


import pandas as pd
import numpy as np
import csv

#           ***Challenge One***
df = pd.DataFrame()
for chunk in pd.read_csv('C:/Users/jerem/Desktop/Project0/COVID_19_Nursing_Home_Data_2021_09_19.csv',
                         usecols=['week_ending', 'federal_provider_number', 'provider_state',
                                  'percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time',
                                  'residents_weekly_confirmed_covid_19'],
                         chunksize=1000000,
                         iterator=True,
                         dtype='object'):
    df = pd.concat([df, chunk], axis=0, ignore_index=False)

xl = pd.read_excel('C:/Users/jerem/Desktop/Project0/Our_Provider_numbers.xlsx', dtype='object')
df2 = pd.merge(df, xl, how='inner', left_on='federal_provider_number', right_on='our affilitied federal provider numbers')
df2['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'] \
    = df2['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'].astype('float')
avgByStatePerWeek = df2.groupby(['week_ending', 'provider_state'], as_index=False)['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'].mean()

challengeOne = [(x, y, z)
                for x, y, z in zip(avgByStatePerWeek['week_ending'],
                                   avgByStatePerWeek['provider_state'],
                                   avgByStatePerWeek['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'])
                if z > float(80)]

challengeOne = pd.DataFrame(challengeOne, columns = ['week_ending', 'provider_state',
                                                     'percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'])
challengeOne.to_csv('C:/Users/jerem/Desktop/Project0/Challenge_One.csv', index=False)
#           ***Challenge One***


#           ***Challenge Two***
df2 = df2.append({'federal_provider_number':'676459', 'residents_weekly_confirmed_covid_19':'0'}, ignore_index=True)
df2['start_of_streak'] = df2['federal_provider_number'].ne(df2['federal_provider_number'].shift(-1)) \
                         | df2['residents_weekly_confirmed_covid_19'].ne('0')
df2['streak_id'] = df2['start_of_streak'].cumsum()
df2['longest_streak'] = df2.groupby(['streak_id']).cumcount() + 1
# print(df2['longest_streak'])

challengeTwo = df2.groupby(['federal_provider_number'], as_index=False)['longest_streak'].max()

challengeTwo.to_csv('C:/Users/jerem/Desktop/Project0/Challenge_Two.csv', index=False)
#           ***Challenge Two***

