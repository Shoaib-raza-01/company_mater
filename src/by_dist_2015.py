"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file


def plot(dist_zip):
    """ploting function"""
    plt.bar(dist_zip.keys(), dist_zip.values())
    # plt.figure(figsize=(12,10))
    plt.xlabel("Districts")
    plt.ylabel("Count of companies")
    plt.title("No of company registration in 2015 by districts")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/by_dist_2015.png')


def execute():
    """main function"""
    dist_zip = {}
    with open('../dataset/dist_zip.csv', 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            dist = row.get('District')
            pin = row.get('Pin Code')
            if dist not in dist_zip:
                dist_zip[dist] = pin

    # print(dist_zip)
    cnt_by_district = {}
    with open('../dataset/MCA_MH.csv', 'r', encoding='ISO-8859-1') as file:
        data = csv.DictReader(file)

        for row in data:
            date_str = row.get('DATE_OF_REGISTRATION')
            date_list = date_str.split('-')

            address_str = row.get('REGISTERED_OFFICE_ADDRESS')
            address_list = address_str.split(" ")

            try:
                year = int(date_list[2])
                if year == 2015:
                    pin = address_list[-1]
                    if pin not in cnt_by_district:
                        cnt_by_district[pin] = 1
                    else:
                        cnt_by_district[pin] += 1
            except Exception:
                pass
    for city, pin in dist_zip.items():
        if pin in cnt_by_district:
            dist_zip[city] = cnt_by_district[pin]
    plot(dist_zip)


execute()
