"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file


def plot(comp_per_year):
    """ploting function """
    plt.bar(comp_per_year.keys(), comp_per_year.values())
    plt.xlabel("Year")
    plt.ylabel("Number of Companies Registered")
    plt.title("Companies registered per Year")
    plt.savefig('../images/reqn_per_year.png')


def execute():
    """creating data for ploting"""
    comp_cnt_by_year = {}
    with open('../dataset/MCA_MH.csv', 'r', encoding='ISO-8859-1') as file:
        data = csv.DictReader(file)
        for row in data:
            date_str = row.get('DATE_OF_REGISTRATION')
            date_list = date_str.split('-')
            # print(date_list)
            # year = int(date_list[2])
            # print(year)
            try:
                year = int(date_list[2])
                if year > 2018:
                    continue
                if year not in comp_cnt_by_year:
                    comp_cnt_by_year[year] = 1
                else:
                    comp_cnt_by_year[year] += 1
            except Exception:
                pass
        # print(comp_cnt_by_year)
    plot(comp_cnt_by_year)


execute()
