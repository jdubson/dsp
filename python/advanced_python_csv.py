import csv
import urllib2
import pandas as pd
import re

url = 'https://raw.githubusercontent.com/jdubson/dsp/master/python/faculty.csv'
data = urllib2.urlopen(url)

def read_data(data):
    faculty_csv = csv.reader(data)

    faculty_data = []

    for row in faculty_csv:
        faculty_data.append(row)

    header = faculty_data[0]
    faculty_data.pop(0)
    faculty_df = pd.DataFrame(faculty_data, columns = header)

    faculty_df[faculty_df.columns[1]] = faculty_df[faculty_df.columns[1]].str.replace('[.]','')
    faculty_df[faculty_df.columns[1]] = faculty_df[faculty_df.columns[1]].str.lstrip()

    return faculty_df


def write_data(parsed_data):
    emails = parsed_data[parsed_data.columns[3]].unique().tolist()
    with open('emails.csv', 'wb') as mycsvfile:
        datawriter = csv.writer(mycsvfile)
        for email in emails:
            datawriter.writerow([email])


df = read_data(data)
write_data(df)
