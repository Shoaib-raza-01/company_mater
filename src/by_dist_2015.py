"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt
# Reading the data from a CSV file

DIST_ZIP= {}
with open('../dataset/dist_zip.csv' , 'r') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        dist = row.get('District')
        pin = row.get('Pin Code')
        if dist not in DIST_ZIP:
            DIST_ZIP[dist] = pin
            
# print(DIST_ZIP)

cnt_by_district = {}
with open('../dataset/MCA_MH.csv', 'r', encoding = 'ISO-8859-1') as file:
    data = csv.DictReader(file)

    for row in data:

        dateStr = row.get('DATE_OF_REGISTRATION')
        dateList = dateStr.split('-')

        addressStr = row.get('REGISTERED_OFFICE_ADDRESS')
        addressList = addressStr.split(" ")

        try:
            year = int(dateList[2])
            if year == 2015:
                pin = addressList[-1]
                if pin not in cnt_by_district:
                    cnt_by_district[pin] = 1
                else:
                    cnt_by_district[pin] += 1
        except:
            pass
# print(cnt_by_district)


for city, pin in DIST_ZIP.items():
    if pin in cnt_by_district:
        DIST_ZIP[city] = cnt_by_district[pin]

# Print the updated dictionary
# print(updated_dict)
# print(len(DIST_ZIP))

plt.bar(DIST_ZIP.keys(), DIST_ZIP.values())
# plt.figure(figsize=(12,10))
plt.xlabel("Districts")
plt.ylabel("Count of companies")
plt.title("No of company registration in 2015 by districts")
plt.xticks(rotation = 90)
plt.savefig('../images/by_dist_2015.png')