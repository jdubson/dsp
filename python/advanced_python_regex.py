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


def degrees(parsed_data):
    degree_types = parsed_data[parsed_data.columns[1]].unique().tolist()
    degree_types = [i.split() for i in degree_types]
    degree_types = [item for sublist in degree_types for item in sublist]
    degree_types = list(set(degree_types))
    degree_types.remove('0')

    tot_degrees = []
    count = 0
    for deg in degree_types:
        has_deg = parsed_data[parsed_data.columns[1]].str.contains(deg)
        for val in has_deg:
            if val == True:
                count = count + 1
        tot_degrees.append((deg,count))
        count = 0

    return tot_degrees


def titles(parsed_data):
    title_types = parsed_data[parsed_data.columns[2]].unique().tolist()
    title_types = [re.sub('..[of|is].Biostatistics', '', i) for i in title_types]
    title_types = list(set(title_types))

    tot_titles = []
    count = 0
    for title in title_types:
        has_title = parsed_data[parsed_data.columns[2]].str.match(title)
        for val in has_title:
            if val == True:
                count = count + 1
        tot_titles.append((title,count))
        count = 0

    return tot_titles


def email_list(parsed_data):
    emails = parsed_data[parsed_data.columns[3]].unique().tolist()

    return emails


def email_domains(parsed_data):
    emails_dom = parsed_data[parsed_data.columns[3]].unique().tolist()
    emails_dom = [re.sub('.*@', '@', i) for i in emails_dom]
    emails_dom = list(set(emails_dom))

    tot_emails_dom = []
    count = 0
    for emails in emails_dom:
        has_email = parsed_data[parsed_data.columns[3]].str.contains(emails)
        for val in has_email:
            if val == True:
                count = count + 1
        emails = re.sub('@','', emails)
        tot_emails_dom.append((emails, count))
        count = 0

    return tot_emails_dom


df = read_data(data)
print degrees(df)
print titles(df)
print email_list(df)
print email_domains(df)
