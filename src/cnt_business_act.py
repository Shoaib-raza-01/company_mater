"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file


with open('../dataset/MCA_MH.csv' , 'r', encoding = 'ISO-8859-1') as file:
    year_count = {}
    business_acctivity_count = {}
    reader = csv.DictReader(file)

    for row in reader:
        dateStr = row.get('DATE_OF_REGISTRATION')
        dateList = dateStr.split('-')

        business_activity = row.get('PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN')

        try:
            if business_activity not in business_acctivity_count:
                business_acctivity_count[business_activity] = 1
            else:
                business_acctivity_count[business_activity] += 1
            year = int(dateList[2])
            if year > 2020:
                continue
            else:
                if year not in year_count:
                    year_count[year] = 1
                else:
                    year_count[year] += 1
        except:
            pass
    sorted_by_year = dict(sorted(year_count.items()))
    # print(sorted_by_year)
    last_10_year_count = dict(list(sorted_by_year.items())[-10:])
    print(last_10_year_count)