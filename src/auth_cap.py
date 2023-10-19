"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file

with open('../dataset/MCA_MH.csv', 'r', encoding = 'ISO-8859-1') as file:
    data = csv.DictReader(file)
    auth_cap = []
    for row in data:
        try:
            cap = row.get('AUTHORIZED_CAP')
            if cap is not None:
                auth_cap.append(int(cap))      
        except Exception as e:
           pass


    # print(auth_cap)
    # Plotting the graph using Matplotlib
    plt.figure(figsize=(12,10))
    bins = [0,5000000, 10000000,50000000, 100000000]
    bin_labels = ['<= 50L', '50L to 1Cr','1Cr to 5Cr','5Cr to 10Cr','> 10Cr']

    plt.hist(auth_cap, bins=bins , edgecolor = 'black',)
    plt.xlabel("Authorized Capacity")
    plt.ylabel("Frequency of Authorized Capacity")
    plt.title("Distribution of Authorized Capacity")
    plt.xticks(bins, bin_labels, rotation= 90)

    plt.savefig('../images/auth_cap.png')
