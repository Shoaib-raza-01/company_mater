"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file

with open('../dataset/MCA_MH.csv', 'r', encoding = 'ISO-8859-1') as file:
    data = csv.DictReader(file)

    comp_cnt_by_year = {}
    for row in data:
        dateStr = row.get('DATE_OF_REGISTRATION')
        dateList = dateStr.split('-')
        # print(dateList)
        # year = int(dateList[2])
        # print(year)
        try:
            year = int(dateList[2])
            if year > 2018:
                continue
            else:
                if year not in comp_cnt_by_year:
                    comp_cnt_by_year[year] = 1
                else:
                    comp_cnt_by_year[year] += 1
        except:
            pass
    # print(comp_cnt_by_year)
    plt.bar(comp_cnt_by_year.keys(),comp_cnt_by_year.values())
    plt.xlabel("Year")
    plt.ylabel("Number of Companies Registered")
    plt.title("Companies registered per Year")
    plt.savefig('../images/reqn_per_year.png')