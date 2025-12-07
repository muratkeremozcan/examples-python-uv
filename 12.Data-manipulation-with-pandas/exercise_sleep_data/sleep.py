import pandas as pd
import os

# import csv
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'sleep_health_data.csv')

df = pd.read_csv(csv_path)

print(df)
print()

# Your client, SleepInc, has shared anonymized sleep data from their hot new sleep tracking app SleepScope. 
# As their data science consultant, your mission is to analyze the lifestyle survey data with Python
# to discover relationships between exercise, gender, occupation, and sleep quality. 
# See if you can identify patterns leading to insights on sleep quality.
# 💾 The data: sleep_health_data.csv
# SleepInc has provided you with an anonymized dataset of sleep and lifestyle metrics for 374 individuals. 
# This dataset contains average values for each person calculated over the past six months. 
# The data is saved as sleep_health_data.csv.

##################

# Which occupation has the lowest average sleep duration? 
# Save this in a string variable called lowest_sleep_occ.
lowest_sleep_occ = df.groupby('Occupation')['Sleep Duration'].mean().idxmin()  # (index)[value]
print("\nOccupation with lowest average sleep duration:", lowest_sleep_occ)

# Which occupation has the lowest average sleep quality?
# Save this in a string variable called lowest_sleep_quality_occ
avg_quality_by_occ = df.groupby('Occupation')['Quality of Sleep'].mean().sort_values()  # (index)[value]
print('\nAverage quality by occupation: \n', avg_quality_by_occ)
lowest_sleep_quality_occ = avg_quality_by_occ.idxmin()
print("\nOccupation with lowest average sleep quality:", lowest_sleep_quality_occ)
print()

# Did the occupation with the lowest sleep duration also have the lowest sleep quality? 
# If so assign a boolean value to variable same_occ variable, True if it is the same occupation, and False if it isn't.
print('\nDid the occupation with the lowest sleep duration also have the lowest sleep quality?')
same_occ = lowest_sleep_occ == lowest_sleep_quality_occ
print(same_occ)
print()

# Let's explore how BMI Category can affect sleep disorder rates. 
# Start by finding what ratio of app users in each BMI Category have been diagnosed with Insomnia. 
# Create a new column indicating if a person has Insomnia

df['Has_Insomnia'] = df['Sleep Disorder'] == 'Insomnia'
# Calculate total people and people with insomnia in each BMI category
bmi_insomnia = df.groupby('BMI Category')['Has_Insomnia'].agg(['sum', 'count'])
print('\nTotal people and people with insomnia in each BMI category:')
print(bmi_insomnia)
print()

# Create a dictionary named: bmi_insomnia_ratios. The key should be the BMI Category as a string, 
# while the value should be the ratio of people in this category with insomnia as a float rounded to two decimal places. Here is an example:
bmi_insomnia_ratios = (bmi_insomnia['sum'] / bmi_insomnia['count']).round(2).to_dict()
print('\nBMI Insomnia Ratios:')
print(bmi_insomnia_ratios)
print()