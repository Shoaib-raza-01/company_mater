"""Importing CSV and Matplotlib"""
import csv
import matplotlib.pyplot as plt


def plot(years, activity, act_cnt):
    """ploting"""
    plt.figure(figsize=(10, 6))
    bottom = [0] * len(years)
    for act in activity:
        values = act_cnt[act]
        plt.bar(years, values, label=act, bottom=bottom)
        bottom = [b + v for b, v in zip(bottom, values)]
    plt.xlabel('Year')
    plt.ylabel('count')
    plt.title('Top 5 activities for last 10 years')
    plt.legend(title='Teams', loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('../images/top_5_for_last_10_yr.png')


def calculate(top_5):
    """modifying the data for plotting"""
    activity = set()
    years = list(top_5.keys())
    for year_data in top_5.values():
        activity.update(year_data.keys())
    activity = sorted(activity)
    act_count = {act: [top_5[year].get(act, 0)
                       for year in years] for act in activity}

    plot(years, activity, act_count)


def execute():
    """execute fun to extract data from file"""
    field = 'PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN'
    with open('../dataset/MCA_MH.csv', 'r', encoding='ISO-8859-1') as file:
        business_acctivity_count = {}
        reader = csv.DictReader(file)

        for row in reader:
            date_str = row.get('DATE_OF_REGISTRATION')
            date_list = date_str.split('-')

            business_activity = row.get(field)

            try:
                year = int(date_list[-1])
                if 2009 <= year <= 2018:
                    if year not in business_acctivity_count:
                        business_acctivity_count[year] = {}
                    if business_activity not in business_acctivity_count[year]:
                        business_acctivity_count[year][business_activity] = 1
                    else:
                        business_acctivity_count[year][business_activity] += 1
            except Exception:
                pass
        top_5_act_year = {}
        for year, year_top_5_per_year in business_acctivity_count.items():
            sorted_activities = sorted(year_top_5_per_year.items(),
                                       key=lambda x: x[1], reverse=True)
            top_5_activities = sorted_activities[:5]
            top_5_act_year[year] = dict(top_5_activities)
        # print(top_5_act_year)
        calculate(top_5_act_year)


execute()
